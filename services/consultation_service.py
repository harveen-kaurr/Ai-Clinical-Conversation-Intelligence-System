from datetime import date

from models.consultation import ConsultationCreate


class ConsultationService:

    REQUIRED_FIELDS = [
        "patient_id",
        "doctor_name",
        "specialization",
        "consultation_date",
        "consultation_time",
        "chief_complaint"
    ]

    @staticmethod
    def validate_consultation(
        consultation_data: dict
    ) -> None:

        for field in ConsultationService.REQUIRED_FIELDS:

            if (
                field not in consultation_data
                or consultation_data[field] is None
                or consultation_data[field] == ""
            ):
                raise ValueError(
                    f"{field} is required"
                )

        followup_date = consultation_data.get(
            "followup_date"
        )

        consultation_date = consultation_data.get(
            "consultation_date"
        )

        if (
            followup_date
            and consultation_date
            and followup_date < consultation_date
        ):
            raise ValueError(
                "Follow-up date cannot be before consultation date"
            )

    @staticmethod
    def create_consultation_payload(
        consultation_data: dict
    ) -> dict:

        payload = consultation_data.copy()

        return payload

    @staticmethod
    def register_consultation(
        consultation_data: dict
    ) -> dict:

        ConsultationService.validate_consultation(
            consultation_data
        )

        payload = (
            ConsultationService.create_consultation_payload(
                consultation_data
            )
        )

        ConsultationCreate(**payload)

        return payload