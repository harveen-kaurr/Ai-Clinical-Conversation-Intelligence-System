from services.consultation_service import (
    ConsultationService
)


def test_valid_consultation():

    data = {
        "patient_id": "a9724b0b-5f09-4705-bbc7-a09917556467",
        "doctor_name": "Dr Rajat",
        "specialization": "Chiropractic",
        "consultation_date": "2026-06-24",
        "consultation_time": "10:00:00",
        "chief_complaint": "Lower Back Pain"
    }

    payload = (
        ConsultationService.register_consultation(
            data
        )
    )

    assert payload["doctor_name"] == "Dr Rajat"


def test_missing_required_field():

    data = {
        "patient_id": "a9724b0b-5f09-4705-bbc7-a09917556467"
    }

    try:
        ConsultationService.register_consultation(
            data
        )

        assert False

    except ValueError:
        assert True