def format_output(extracted: dict) -> dict:
    if not extracted.get("success"):
        return extracted

    data = extracted["data"]

    # Ensure all expected fields exist
    defaults = {
        "patient_age": None,
        "patient_gender": None,
        "admission_reason": None,
        "conditions": [],
        "medications": [],
        "blood_pressure": None,
        "key_vitals": {},
        "hospital_stay_days": None,
        "discharge_plan": None,
        "follow_up": None,
        "document_type": "Clinical Note"
    }

    for key, default in defaults.items():
        if key not in data:
            data[key] = default

    return {"success": True, "data": data}
