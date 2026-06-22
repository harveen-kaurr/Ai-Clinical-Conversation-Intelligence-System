def validate_pain_assessment(data):

    errors = []

    # Patient ID validation
    if not data.get("patient_id"):
        errors.append("Patient ID is required")

    # Pain Areas validation
    if not data.get("pain_areas"):
        errors.append("Pain area is required")

    # Pain Severity validation
    pain_severity = data.get("pain_severity")

    if pain_severity is None:
        errors.append("Pain severity is required")

    elif pain_severity < 0 or pain_severity > 10:
        errors.append(
            "Pain severity must be between 0 and 10"
        )

    # Posture validation
    if not data.get("posture"):
        errors.append("Posture is required")

    return errors