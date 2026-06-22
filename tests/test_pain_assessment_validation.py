from utils.validate_pain_assessment import (
    validate_pain_assessment
)

assessment = {
    "patient_id": "123",
    "pain_areas": "Lower Back",
    "pain_severity": 8,
    "posture": "Normal"
}

errors = validate_pain_assessment(assessment)

if len(errors) == 0:
    print("Validation Passed")
else:
    print("Validation Failed")
    print(errors)