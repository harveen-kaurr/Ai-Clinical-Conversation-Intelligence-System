from datetime import datetime
from models.patient import PatientCreate
from utils.bmi_calc import get_bmi_data
from utils.validation import (
    validate_age,
    validate_email,
    validate_emergency_contact,
    validate_gender,
    validate_phone_number,
    validate_alternate_phone_number,
    validate_required_fields,
    validate_duplicate_patient
)
class PatientService:
    REQUIRED_FIELDS = [
        "patient_name",
        "gender",
        "age",
        "phone_number"
    ]
    @staticmethod
    def validate_patient(
        patient_data: dict,
        supabase=None,
        exclude_id: str = None
    ) -> None:

        valid, message = validate_required_fields(
            patient_data,
            PatientService.REQUIRED_FIELDS
        )

        if not valid:
            raise ValueError(message)

        valid, message = validate_phone_number(
            patient_data["phone_number"]
        )

        if not valid:
            raise ValueError(message)

        valid, message = validate_alternate_phone_number(
            patient_data.get(
                "alternate_phone_number"
            )
        )

        if not valid:
            raise ValueError(message)

        valid, message = validate_email(
            patient_data.get("email")
        )

        if not valid:
            raise ValueError(message)

        valid, message = validate_age(
            patient_data["age"]
        )

        if not valid:
            raise ValueError(message)

        valid, message = validate_gender(
            patient_data["gender"]
        )

        if not valid:
            raise ValueError(message)

        valid, message = validate_emergency_contact(
            patient_data.get("emergency_contact")
        )

        if not valid:
            raise ValueError(message)

        if supabase:

            valid, message = (
                validate_duplicate_patient(
                    supabase=supabase,
                    phone_number=patient_data[
                        "phone_number"
                    ],
                    exclude_id=exclude_id
                )
            )

            if not valid:
                raise ValueError(message)

    @staticmethod
    def create_patient_payload(
        patient_data: dict,
        patient_id: str
    ) -> dict:

        payload = patient_data.copy()

        # payload["patient_id"] = patient_id

        height = payload.get("height_cm")
        weight = payload.get("weight_kg")

        if height and weight:

            bmi_data = get_bmi_data(
                weight_kg=weight,
                height_cm=height
            )

            payload["bmi"] = bmi_data["bmi"]
            payload["bmi_category"] = bmi_data["category"]

        return payload

    @staticmethod
    def register_patient(
        patient_data: dict,
        supabase=None
    ) -> dict:

        PatientService.validate_patient(
            patient_data=patient_data,
            supabase=supabase
        )

        payload = (
            PatientService.create_patient_payload(
                patient_data,
                None
            )
        )
        PatientCreate(**payload)
        return payload