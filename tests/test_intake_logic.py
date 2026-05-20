from src.logic import create_field_packet


def test_sample_note_extraction_and_flags():
    note = (
        "Went to Conestoga today. R-36 had 3 punctures near drain. "
        "Patched with TPO. Water still ponding. Need to check next rain. "
        "Crew was Mike and Luis, 7 hours."
    )
    packet, warning = create_field_packet(note)

    assert packet["job_name"] == "Conestoga"
    assert "3 punctures" in packet["issues_found"]
    assert "water ponding" in packet["issues_found"]
    assert any("R-36" in item for item in packet["issues_found"])
    assert "TPO" in packet["materials_mentioned"]
    assert "check next rain" in packet["follow_up_needed"]
    assert "customer_name" in packet["missing_information"]
    assert "site_address" in packet["missing_information"]
    assert "final_completion_status" in packet["missing_information"]
    assert packet["human_review_required"] is True
    assert "Human review required" in warning
