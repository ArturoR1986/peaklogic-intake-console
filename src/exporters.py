import json
from typing import Dict


SECTION_TITLES = [
    "Job Information",
    "Intake Classification",
    "Field Summary",
    "Work Completed",
    "Issues Found",
    "Materials Mentioned",
    "Photos / Visual References",
    "Internal Notes",
    "Customer-Facing Draft Notes",
    "Missing Information",
    "Follow-Up Needs",
    "Human Review Required",
]


def packet_to_json(packet: Dict) -> str:
    return json.dumps(packet, indent=2)


def packet_to_markdown(packet: Dict) -> str:
    job = packet["job_information"]
    customer = packet["customer_facing_draft"]

    sections = [
        "# Reviewable Field Packet",
        "## Job Information",
        _job_information(job),
        "## Intake Classification",
        packet["intake_classification"],
        "## Field Summary",
        packet["field_summary"],
        "## Work Completed",
        _bullets(packet["work_completed"]),
        "## Issues Found",
        _bullets(packet["issues_found"]),
        "## Materials Mentioned",
        _bullets(packet["materials_mentioned"]),
        "## Photos / Visual References",
        _bullets(packet["photos_or_visual_references"]),
        "## Internal Notes",
        _bullets(packet["internal_notes"]),
        "## Customer-Facing Draft Notes",
        customer["warning"] + "\n\n" + _bullets(customer["notes"]),
        "## Missing Information",
        _bullets(packet["missing_information"]),
        "## Follow-Up Needs",
        _bullets(packet["follow_up_needs"]),
        "## Human Review Required",
        _bullets(packet["human_review_required"]),
    ]
    return "\n\n".join(sections) + "\n"


def _job_information(job: Dict) -> str:
    return "\n".join(
        [
            f"- Job Name: {job['job_name']}",
            f"- Address: {job['address']}",
            f"- Date: {job['date']}",
            f"- Foreman: {job['foreman']}",
            f"- Crew: {', '.join(job['crew']) if job['crew'] else 'Missing'}",
        ]
    )


def _bullets(items: list) -> str:
    if not items:
        return "- Missing"
    return "\n".join(f"- {item}" for item in items)
