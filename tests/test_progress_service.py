from datetime import date

import pytest

from services.progress_service import ProgressService


def valid_progress_data():

    return {

        "patient_id": "93411e17-7d02-454c-88f5-660e4377117f",

        "treatment_id": "1c476fff-2ffc-415b-a7f7-4411e4d65eeb",

        "session_number": 1,

        "progress_date": date.today(),

        "previous_pain_score": 8,

        "current_pain_score": 5,

        "mobility_improvement": 60,

        "sleep_quality": 8,

        "numbness_improvement": 50,

        "range_of_motion": 65,

        "patient_feedback": "Pain has reduced.",

        "practitioner_remark": "Patient improving."
    }


def test_register_progress():

    payload = ProgressService.register_progress(

        valid_progress_data()

    )

    assert payload["session_number"] == 1

    assert payload["overall_recovery_status"] == "Moderate"


def test_missing_patient_id():

    data = valid_progress_data()

    del data["patient_id"]

    with pytest.raises(ValueError):

        ProgressService.register_progress(data)


def test_invalid_previous_pain_score():

    data = valid_progress_data()

    data["previous_pain_score"] = 20

    with pytest.raises(ValueError):

        ProgressService.register_progress(data)


def test_invalid_current_pain_score():

    data = valid_progress_data()

    data["current_pain_score"] = -1

    with pytest.raises(ValueError):

        ProgressService.register_progress(data)


def test_recovery_status():

    data = valid_progress_data()

    status = ProgressService.calculate_recovery_status(

        data

    )

    assert status == "Moderate"