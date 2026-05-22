import re
from typing import Iterable, List, Optional

from src.intake_classifier import classify_intake
from src.models import CustomerFacingDraft, FieldIntake, FieldPacket, JobMetadata, MISSING, UNKNOWN


MATERIAL_KEYWORDS = [
    "TPO",
    "PVC",
    "EPDM",
    "membrane",
    "patch",
    "patches",
    "sealant",
    "drain",
    "flashing",
    "insulation",
    "rock wool",
    "pipe boot",
    "termination bar",
]

INTERNAL_SIGNALS = [
    "customer is upset",
    "upset",
    "we forgot",
    "forgot material",
    "didn't have",
    "did not have",
    "do not answer",
    "don't answer",
    "manager to review",
]

FOLLOW_UP_SIGNALS = [
    "check next rain",
    "follow up",
    "needs review",
    "need service manager",
    "return visit",
    "not finished",
    "need to order",
    "need inspection",
]


def _clean(value: Optional[str]) -> str:
    if value is None:
        return MISSING
    value = value.strip()
    return value if value else MISSING


def _crew_list(crew: Optional[Iterable[str] | str]) -> List[str]:
    if crew is None:
        return []
    if isinstance(crew, str):
        parts = re.split(r",| and ", crew)
    else:
        parts = list(crew)
    return [part.strip() for part in parts if part and part.strip()]


def build_metadata(
    job_name: Optional[str] = None,
    address: Optional[str] = None,
    date: Optional[str] = None,
    foreman: Optional[str] = None,
    crew: Optional[Iterable[str] | str] = None,
) -> JobMetadata:
    return JobMetadata(
        job_name=_clean(job_name),
        address=_clean(address),
        date=_clean(date),
        foreman=_clean(foreman),
        crew=_crew_list(crew),
    )


def build_field_intake(raw_input: str, metadata: JobMetadata) -> FieldIntake:
    return FieldIntake(
        raw_input=raw_input,
        metadata=metadata,
        intake_type=classify_intake(raw_input),
    )


def build_field_packet(raw_input: str, metadata: Optional[JobMetadata] = None) -> FieldPacket:
    metadata = metadata or build_metadata()
    intake = build_field_intake(raw_input, metadata)

    work_completed = _extract_work_completed(raw_input)
    issues_found = _extract_issues(raw_input)
    materials = _extract_materials(raw_input)
    visuals = _extract_visual_references(raw_input)
    internal = _extract_internal_notes(raw_input)
    followups = _extract_followups(raw_input)
    missing = _missing_information(metadata, raw_input, work_completed, issues_found)
    human_review = _human_review_required(raw_input, intake.intake_type)

    return FieldPacket(
        job_information=metadata,
        intake_classification=intake.intake_type,
        field_summary=_field_summary(raw_input),
        work_completed=work_completed,
        issues_found=issues_found,
        materials_mentioned=materials,
        photos_or_visual_references=visuals,
        internal_notes=internal,
        customer_facing_draft=CustomerFacingDraft(notes=_customer_notes(work_completed, issues_found, followups)),
        missing_information=missing,
        follow_up_needs=followups,
        human_review_required=human_review,
    )


def _sentences(raw_input: str) -> List[str]:
    return [part.strip(" .\n\t") for part in re.split(r"[.\n]+", raw_input) if part.strip()]


def _field_summary(raw_input: str) -> str:
    sentences = _sentences(raw_input)
    if not sentences:
        return MISSING
    return sentences[0]


def _extract_work_completed(raw_input: str) -> List[str]:
    signals = ["patched", "sealed", "finished", "repaired", "installed", "used", "completed"]
    return [sentence for sentence in _sentences(raw_input) if any(signal in sentence.lower() for signal in signals)] or [UNKNOWN]


def _extract_issues(raw_input: str) -> List[str]:
    issues: List[str] = []
    for sentence in _sentences(raw_input):
        lower = sentence.lower()
        if any(word in lower for word in ["leak", "water", "wet", "puncture", "ponding", "damage", "crack", "source"]):
            if "source" in lower and any(word in lower for word in ["not sure", "unknown", "unclear"]):
                issues.append(f"{sentence}; leak cause: {UNKNOWN}")
            else:
                issues.append(sentence)
    return issues or [UNKNOWN]


def _extract_materials(raw_input: str) -> List[str]:
    lower = raw_input.lower()
    found = []
    for material in MATERIAL_KEYWORDS:
        if material.lower() in lower:
            found.append(material)
    return sorted(set(found), key=str.lower) or [UNKNOWN]


def _extract_visual_references(raw_input: str) -> List[str]:
    visuals = []
    for sentence in _sentences(raw_input):
        lower = sentence.lower()
        if any(word in lower for word in ["photo", "picture", "video", "visual"]):
            visuals.append(sentence)
    return visuals or [UNKNOWN]


def _extract_internal_notes(raw_input: str) -> List[str]:
    notes = []
    for sentence in _sentences(raw_input):
        lower = sentence.lower()
        if any(signal in lower for signal in INTERNAL_SIGNALS):
            notes.append(sentence)
    return notes or ["No internal-only notes identified."]


def _extract_followups(raw_input: str) -> List[str]:
    followups = []
    for sentence in _sentences(raw_input):
        lower = sentence.lower()
        if any(signal in lower for signal in FOLLOW_UP_SIGNALS):
            followups.append(sentence)
    return followups or [UNKNOWN]


def _missing_information(
    metadata: JobMetadata,
    raw_input: str,
    work_completed: List[str],
    issues_found: List[str],
) -> List[str]:
    missing = []
    for field_name in ["job_name", "address", "date", "foreman"]:
        if getattr(metadata, field_name) == MISSING:
            missing.append(field_name)
    if not metadata.crew:
        missing.append("crew")
    if work_completed == [UNKNOWN]:
        missing.append("work_completed")
    if issues_found == [UNKNOWN]:
        missing.append("issues_found")
    if re.search(r"leak|water|source|ceiling", raw_input, re.IGNORECASE):
        missing.append("leak_cause_or_source")
    return missing


def _human_review_required(raw_input: str, intake_type: str) -> List[str]:
    review = ["Customer-facing draft notes require human review before sending."]
    lower = raw_input.lower()
    if "leak" in lower or "source" in lower or intake_type == "Leak Investigation":
        review.append("Leak cause/source must remain Unknown until confirmed by a qualified reviewer.")
    if any(word in lower for word in ["warranty", "legal", "price", "pricing", "safety", "liability"]):
        review.append("Warranty, legal, pricing, safety, and liability claims must be reviewed and excluded from draft notes.")
    return review


def _customer_notes(work_completed: List[str], issues_found: List[str], followups: List[str]) -> List[str]:
    notes = []
    safe_work = [item for item in work_completed if item != UNKNOWN]
    safe_issues = [item for item in issues_found if item != UNKNOWN]
    safe_followups = [item for item in followups if item != UNKNOWN]

    if safe_work:
        notes.append("Documented work: " + "; ".join(safe_work))
    if safe_issues:
        notes.append("Observed items: " + "; ".join(safe_issues))
    if safe_followups:
        notes.append("Follow-up noted: " + "; ".join(safe_followups))
    if not notes:
        notes.append("Field update received; details require office review.")
    return notes
