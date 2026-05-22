from dataclasses import asdict, dataclass, field
from typing import List


MISSING = "Missing"
UNKNOWN = "Unknown"
REVIEW_WARNING = "Draft only. Requires human review before sending."


@dataclass
class JobMetadata:
    job_name: str = MISSING
    address: str = MISSING
    date: str = MISSING
    foreman: str = MISSING
    crew: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class FieldIntake:
    raw_input: str
    metadata: JobMetadata
    intake_type: str

    def to_dict(self) -> dict:
        return {
            "raw_input": self.raw_input,
            "metadata": self.metadata.to_dict(),
            "intake_type": self.intake_type,
        }


@dataclass
class CustomerFacingDraft:
    warning: str = REVIEW_WARNING
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class FieldPacket:
    job_information: JobMetadata
    intake_classification: str
    field_summary: str
    work_completed: List[str] = field(default_factory=list)
    issues_found: List[str] = field(default_factory=list)
    materials_mentioned: List[str] = field(default_factory=list)
    photos_or_visual_references: List[str] = field(default_factory=list)
    internal_notes: List[str] = field(default_factory=list)
    customer_facing_draft: CustomerFacingDraft = field(default_factory=CustomerFacingDraft)
    missing_information: List[str] = field(default_factory=list)
    follow_up_needs: List[str] = field(default_factory=list)
    human_review_required: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        data = asdict(self)
        data["job_information"] = self.job_information.to_dict()
        data["customer_facing_draft"] = self.customer_facing_draft.to_dict()
        return data
