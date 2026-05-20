from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from typing import List

MISSING_VALUE = "Missing"
DEFAULT_STATUS = "New"


@dataclass
class FieldPacket:
    intake_id: str
    date_created: str
    job_name: str = MISSING_VALUE
    customer_name: str = MISSING_VALUE
    site_address: str = MISSING_VALUE
    foreman_or_sender: str = MISSING_VALUE
    crew_members: List[str] = field(default_factory=list)
    raw_field_note: str = ""
    input_type: str = "text"
    work_completed: str = MISSING_VALUE
    issues_found: List[str] = field(default_factory=list)
    materials_mentioned: List[str] = field(default_factory=list)
    follow_up_needed: List[str] = field(default_factory=list)
    missing_information: List[str] = field(default_factory=list)
    internal_notes: str = ""
    internal_summary: str = ""
    customer_facing_notes: str = ""
    human_review_required: bool = True
    status: str = DEFAULT_STATUS

    def to_dict(self) -> dict:
        return asdict(self)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
