INTAKE_TYPES = {
    "daily": "Daily Field Report",
    "repair": "Repair Update",
    "leak": "Leak Investigation",
    "inspection": "Inspection Note",
    "material": "Material / Follow-Up Note",
    "unknown": "Unknown / Needs Review",
}


def classify_intake(raw_input: str) -> str:
    text = raw_input.lower()
    if any(word in text for word in ["leak", "water coming", "water in", "ceiling", "source"]):
        return INTAKE_TYPES["leak"]
    if any(word in text for word in ["patched", "repair", "fixed", "sealed", "flashing"]):
        return INTAKE_TYPES["repair"]
    if any(word in text for word in ["inspection", "inspect", "walked", "observed"]):
        return INTAKE_TYPES["inspection"]
    if any(word in text for word in ["material", "materials", "need", "order", "truck", "follow up"]):
        return INTAKE_TYPES["material"]
    if any(word in text for word in ["today", "crew", "hours", "finished"]):
        return INTAKE_TYPES["daily"]
    return INTAKE_TYPES["unknown"]
