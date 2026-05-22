from src.logic import create_field_packet
from src.models import REVIEW_WARNING


def test_missing_metadata_still_creates_packet():
    packet, warning = create_field_packet("Patched with TPO near drain.")

    assert packet["job_information"]["job_name"] == "Missing"
    assert "job_name" in packet["missing_information"]
    assert "TPO" in packet["materials_mentioned"]
    assert warning == REVIEW_WARNING


def test_unknown_leak_cause_is_not_finalized():
    note = "Customer said leak near office ceiling. Not sure if old pipe boot is the source."
    packet, _ = create_field_packet(note, job_name="Warehouse")

    assert packet["intake_classification"] == "Leak Investigation"
    assert any("Unknown" in issue for issue in packet["issues_found"])
    assert any("Leak cause/source" in item for item in packet["human_review_required"])


def test_internal_notes_stay_out_of_customer_draft():
    note = "Customer is upset. We didn't have the right boot on truck. Took photos."
    packet, _ = create_field_packet(note)
    draft_notes = " ".join(packet["customer_facing_draft"]["notes"]).lower()

    assert any("upset" in note.lower() for note in packet["internal_notes"])
    assert "upset" not in draft_notes
    assert "didn't have" not in draft_notes
    assert packet["customer_facing_draft"]["warning"] == REVIEW_WARNING


def test_metadata_accepts_optional_fields():
    packet, _ = create_field_packet(
        "Finished curb flashing at south section. Used TPO patches.",
        job_name="South Curb",
        address="123 Roof Ave",
        date="2026-05-22",
        foreman="Carlos",
        crew="Ana, Jose",
    )

    assert packet["job_information"]["foreman"] == "Carlos"
    assert packet["job_information"]["crew"] == ["Ana", "Jose"]
    assert "foreman" not in packet["missing_information"]
