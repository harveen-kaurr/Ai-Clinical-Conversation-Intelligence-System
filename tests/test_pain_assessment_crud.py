from services.pain_assessment_crud import (
    get_all_assessments,
    get_assessment_by_id,
    create_assessment,
    update_assessment,
    delete_assessment
)

# READ ALL
assessments = get_all_assessments()

print("\n===== READ ALL =====")
print(f"Total Assessments: {len(assessments)}")

# CREATE
new_assessment = {
    "patient_id": "05421dc7-1e12-4f7e-a8f7-6bc763e6cfe2",
    "pain_areas": "Lower Back",
    "pain_severity": 8,
    "posture": "Normal",
    "notes": "Pain while sitting"
}

created = create_assessment(
    new_assessment
)

print("\n===== CREATE =====")
print(
    f"Assessment ID: "
    f"{created[0]['assessment_id']}"
)

assessment_id = created[0]["assessment_id"]

# READ BY ID
assessment = get_assessment_by_id(
    assessment_id
)

print("\n===== READ BY ID =====")
print(
    f"Pain Area: "
    f"{assessment[0]['pain_areas']}"
)

# UPDATE
updated = update_assessment(
    assessment_id,
    {
        "pain_severity": 5
    }
)

print("\n===== UPDATE =====")
print(
    f"Updated Severity: "
    f"{updated[0]['pain_severity']}"
)

# DELETE
deleted = delete_assessment(
    assessment_id
)

print("\n===== DELETE =====")
print(
    f"Deleted Assessment: "
    f"{deleted[0]['assessment_id']}"
)