from models.treatment import (
    TreatmentCreate
)


class TreatmentService:

    REQUIRED_FIELDS = [

        "consultation_id",

        "treatment_type",

        "session_date"
    ]

    @staticmethod
    def validate_treatment(

        treatment_data: dict

    ) -> None:

        for field in (

            TreatmentService.REQUIRED_FIELDS

        ):

            if (

                field not in treatment_data

                or treatment_data[field] is None

                or treatment_data[field] == ""

            ):

                raise ValueError(

                    f"{field} is required"

                )

    @staticmethod
    def create_treatment_payload(

        treatment_data: dict

    ) -> dict:

        payload = (

            treatment_data.copy()

        )

        return payload

    @staticmethod
    def register_treatment(

        treatment_data: dict

    ) -> dict:

        TreatmentService.validate_treatment(

            treatment_data

        )

        payload = (

            TreatmentService.create_treatment_payload(

                treatment_data

            )

        )

        TreatmentCreate(

            **payload

        )

        return payload