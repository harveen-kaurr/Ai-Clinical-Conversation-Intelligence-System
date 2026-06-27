from datetime import date

from services.progress_service import ProgressService
from services.progress_crud import (
    create_progress,
    get_all_progress,
    get_progress_by_id,
    search_progress
)

# Replace these UUIDs with existing values from your database

PATIENT_ID = "93411e17-7d02-454c-88f5-660e4377117f"
TREATMENT_ID = "1c476fff-2ffc-415b-a7f7-4411e4d65eeb"

progress_data = {

    "patient_id": PATIENT_ID,

    "treatment_id": TREATMENT_ID,

    "session_number": 1,

    "progress_date": date.today(),

    "previous_pain_score": 8,

    "current_pain_score": 5,

    "mobility_improvement": 60,

    "sleep_quality": 8,

    "numbness_improvement": 50,

    "range_of_motion": 65,

    "patient_feedback": "Pain has reduced significantly.",

    "practitioner_remark": "Patient is responding well."

}

print("\nCreating Progress Record...\n")

payload = ProgressService.register_progress(
    progress_data
)

result = create_progress(
    payload
)

print(result)

print("\nFetching All Progress Records...\n")

records = get_all_progress()

print(records)

if records:

    progress_id = records[0]["progress_id"]

    print("\nFetching Progress By ID...\n")

    print(
        get_progress_by_id(
            progress_id
        )
    )

print("\nSearching Patient Progress...\n")

print(
    search_progress(
        patient_id=PATIENT_ID
    )
)