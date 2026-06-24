# demo_service.py

from services.consultation_service import (
    ConsultationService
)

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

print(payload)