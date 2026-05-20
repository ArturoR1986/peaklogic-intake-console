import re
import uuid
from typing import Dict, List

from src.human_output import (
    REVIEW_WARNING,
    build_missing_info_requests,
    generate_customer_facing_draft,
    generate_internal_summary,
)
from src.schemas import FieldPacket, utc_now_iso

MATERIAL_KEYWORDS = [
    "tpo", "pvc", "epdm", "sarnafil", "membrane", "patch", "sealant", "drain", "flashing", "insulation", "rock wool"
]
FOLLOW_UP_SIGNALS = [
    "check next rain", "follow up", "needs review", "needs inspection", "water still ponding", "return visit", "not finished"
]


def _detect_materials(text: str) -> List[str]:
    lower = text.lower()
    return sorted({m.upper() if m in {"tpo", "pvc", "epdm"} else m for m in MATERIAL_KEYWORDS if m in lower})


def _detect_followups(text: str) -> List[str]:
    lower = text.lower()
    return [signal for signal in FOLLOW_UP_SIGNALS if signal in lower]


def _detect_issues(text: str) -> List[str]:
    issues = []
    puncture_match = re.search(r"(\d+)\s+punctures?", text, re.IGNORECASE)
    if puncture_match:
        issues.append(f"{puncture_match.group(1)} punctures")
    if re.search(r"ponding", text, re.IGNORECASE):
        issues.append("water ponding")
    loc = re.search(r"(R-\d+).+near drain", text, re.IGNORECASE)
    if loc:
        issues.append(f"{loc.group(1)} near drain")
    return issues


def _detect_job_name(text: str) -> str:
    match = re.search(r"Went to\s+([A-Za-z0-9-]+)", text)
    return match.group(1) if match else "Missing"


def _detect_crew(text: str) -> List[str]:
    match = re.search(r"Crew was\s+([A-Za-z\s,]+?),\s*\d+\s*hours", text, re.IGNORECASE)
    if not match:
        return []
    names = re.split(r",| and ", match.group(1))
    return [n.strip() for n in names if n.strip()]


def create_field_packet(raw_field_note: str, input_type: str = "text") -> Dict:
    packet = FieldPacket(
        intake_id=str(uuid.uuid4()),
        date_created=utc_now_iso(),
        raw_field_note=raw_field_note,
        input_type=input_type,
        job_name=_detect_job_name(raw_field_note),
        crew_members=_detect_crew(raw_field_note),
        issues_found=_detect_issues(raw_field_note),
        materials_mentioned=_detect_materials(raw_field_note),
        follow_up_needed=_detect_followups(raw_field_note),
        work_completed="Patched with TPO" if re.search(r"patched with tpo", raw_field_note, re.IGNORECASE) else "Missing",
        status="Needs Info",
    )

    missing = []
    for fld in ["customer_name", "site_address", "foreman_or_sender"]:
        if getattr(packet, fld) == "Missing":
            missing.append(fld)
    if not re.search(r"(complete|finished)", raw_field_note, re.IGNORECASE):
        missing.append("final_completion_status")
    packet.missing_information = missing

    packet.internal_notes = build_missing_info_requests(packet.missing_information)
    packet.internal_summary = generate_internal_summary(packet.to_dict())
    packet.customer_facing_notes = generate_customer_facing_draft(packet.to_dict())
    packet.human_review_required = True

    return packet.to_dict(), REVIEW_WARNING
