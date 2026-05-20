from typing import Dict, List


REVIEW_WARNING = (
    "Human review required before customer use. Draft content may be incomplete or uncertain."
)


def generate_internal_summary(packet: Dict) -> str:
    issues = ", ".join(packet.get("issues_found") or ["no explicit issue details captured"])
    materials = ", ".join(packet.get("materials_mentioned") or ["no materials captured"])
    followups = ", ".join(packet.get("follow_up_needed") or ["no explicit follow-up captured"])
    crew = ", ".join(packet.get("crew_members") or ["crew not specified"])
    return (
        f"Job: {packet.get('job_name', 'Missing')}. "
        f"Issues observed: {issues}. "
        f"Materials mentioned: {materials}. "
        f"Follow-up signals: {followups}. "
        f"Crew noted: {crew}."
    )


def generate_customer_facing_draft(packet: Dict) -> str:
    issues = ", ".join(packet.get("issues_found") or ["items under review"])
    followups = ", ".join(packet.get("follow_up_needed") or ["next steps under review"])
    return (
        "DRAFT - For customer review after team approval: "
        f"Our team documented the following observed items: {issues}. "
        f"Planned or suggested follow-up: {followups}. "
        "This is a preliminary update and requires human confirmation."
    )


def build_missing_info_requests(missing_information: List[str]) -> str:
    if not missing_information:
        return "No missing information flagged from the provided note."
    return "Please confirm the following missing information: " + ", ".join(missing_information) + "."
