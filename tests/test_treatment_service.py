from services.treatment_service import (
    TreatmentService
)


def print_result(
    title,
    success,
    message
):

    print("\n" + "=" * 55)

    print(title)

    print("=" * 55)

    if success:

        print(
            f"✅ PASS : {message}"
        )

    else:

        print(
            f"❌ FAIL : {message}"
        )


def test_valid_treatment():

    try:

        treatment = {

            "consultation_id":
                "12345678-1234-1234-1234-123456789012",

            "treatment_type":
                "Physiotherapy",

            "treatment_plan":
                "Strengthening exercises",

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
                "Patient responded well."
        }

        TreatmentService.register_treatment(
            treatment
        )

        print_result(
            "VALID TREATMENT TEST",
            True,
            "Treatment validated successfully."
        )

    except Exception as e:

        print_result(
            "VALID TREATMENT TEST",
            False,
            str(e)
        )


def test_missing_consultation_id():

    try:

        treatment = {

            "treatment_type":
                "Physiotherapy",

            "session_date":
                "2026-06-25"
        }

        TreatmentService.register_treatment(
            treatment
        )

        print_result(
            "MISSING CONSULTATION ID",
            False,
            "Validation should have failed."
        )

    except Exception as e:

        print_result(
            "MISSING CONSULTATION ID",
            True,
            str(e)
        )


def test_missing_treatment_type():

    try:

        treatment = {

            "consultation_id":
                "12345678-1234-1234-1234-123456789012",

            "session_date":
                "2026-06-25"
        }

        TreatmentService.register_treatment(
            treatment
        )

        print_result(
            "MISSING TREATMENT TYPE",
            False,
            "Validation should have failed."
        )

    except Exception as e:

        print_result(
            "MISSING TREATMENT TYPE",
            True,
            str(e)
        )


def test_missing_session_date():

    try:

        treatment = {

            "consultation_id":
                "12345678-1234-1234-1234-123456789012",

            "treatment_type":
                "Physiotherapy"
        }

        TreatmentService.register_treatment(
            treatment
        )

        print_result(
            "MISSING SESSION DATE",
            False,
            "Validation should have failed."
        )

    except Exception as e:

        print_result(
            "MISSING SESSION DATE",
            True,
            str(e)
        )


if __name__ == "__main__":

    print("\n")
    print("=" * 55)
    print("TREATMENT SERVICE TEST REPORT")
    print("=" * 55)

    test_valid_treatment()

    test_missing_consultation_id()

    test_missing_treatment_type()

    test_missing_session_date()

    print("\n")
    print("=" * 55)
    print("ALL TESTS COMPLETED")
    print("=" * 55)