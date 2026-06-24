from services.patient_service import (
    PatientService
)


def test_patient_registration():

    patient = (
        PatientService
        .register_patient(
            patient_data={
                "patient_name": "Rajat Sharma",
                "gender": "Male",
                "age": 35,
                "phone_number": "9876543210",
                "height_cm": 175,
                "weight_kg": 78
            }
        )
    )

    assert (
        patient["patient_name"]
        == "Rajat Sharma"
    )

    assert (
        patient["bmi"]
        > 0
    )

    assert (
        patient["bmi_category"]
        is not None
    )