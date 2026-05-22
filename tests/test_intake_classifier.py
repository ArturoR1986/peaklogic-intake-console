from src.intake_classifier import classify_intake


def test_leak_terms_classify_as_leak_investigation():
    result = classify_intake("Customer said leak near office ceiling and water is coming in.")

    assert result == "Leak Investigation"


def test_unknown_when_no_signal_present():
    result = classify_intake("Quick note from the field.")

    assert result == "Unknown / Needs Review"
