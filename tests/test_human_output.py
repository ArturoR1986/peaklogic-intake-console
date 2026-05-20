from src.logic import create_field_packet


def test_customer_draft_marked_and_no_internal_leakage_phrase():
    note = (
        "Went to Conestoga today. R-36 had 3 punctures near drain. "
        "Patched with TPO. Water still ponding. Need to check next rain."
    )
    packet, _ = create_field_packet(note)
    customer = packet["customer_facing_notes"]

    assert customer.startswith("DRAFT")
    assert "internal" not in customer.lower()
    assert "requires human confirmation" in customer
    assert packet["internal_summary"]
