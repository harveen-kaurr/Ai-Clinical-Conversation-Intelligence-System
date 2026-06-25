from services.treatment_service import (
    TreatmentService
)


treatment = {

    "consultation_id":
        "12345678-1234-1234-1234-123456789012",

    "treatment_type":
        "Physiotherapy",

    "treatment_plan":
        "Strengthening exercises for lower back muscles.",

    "medication":
        "Ibuprofen",

    "session_number":
        1,

    "session_date":
        "2026-06-25",

    "therapist_name":
        "Dr. Smith",

    "treatment_status":
        "Ongoing",

    "followup_required":
        True,

    "notes":
        "Patient responded well to the first session."
}


try:

    payload = (
        TreatmentService.register_treatment(
            treatment
        )
    )

    print("\n" + "=" * 60)
    print("TREATMENT SERVICE DEMO")
    print("=" * 60)

    print(
        "\n✅ Treatment Registered Successfully!\n"
    )

    for key, value in payload.items():

        print(
            f"{key:22}: {value}"
        )

    print("\n" + "=" * 60)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("=" * 60)

except Exception as e:

    print("\n" + "=" * 60)
    print("TREATMENT SERVICE DEMO")
    print("=" * 60)

    print(
        f"\n❌ Error : {e}"
    )

    print("\n" + "=" * 60)