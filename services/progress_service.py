from models.progress import ProgressCreate
from services.progress_analytics import ProgressAnalytics


class ProgressService:

    REQUIRED_FIELDS = [

        "patient_id",

        "treatment_id",

        "session_number",

        "progress_date",

        "previous_pain_score",

        "current_pain_score"

    ]

    @staticmethod
    def validate_progress(

        progress_data: dict

    ) -> None:

        for field in (

            ProgressService.REQUIRED_FIELDS

        ):

            if (

                field not in progress_data

                or progress_data[field] is None

                or progress_data[field] == ""

            ):

                raise ValueError(

                    f"{field} is required"

                )

        if not (

            0 <= progress_data["previous_pain_score"] <= 10

        ):

            raise ValueError(

                "Previous pain score must be between 0 and 10"

            )

        if not (

            0 <= progress_data["current_pain_score"] <= 10

        ):

            raise ValueError(

                "Current pain score must be between 0 and 10"

            )

    @staticmethod
    def create_progress_payload(

        progress_data: dict

    ) -> dict:

        payload = (

            progress_data.copy()

        )

        if hasattr(

            payload["progress_date"],

            "isoformat"

        ):

            payload["progress_date"] = (

                payload["progress_date"]

                .isoformat()

            )

        score = (

            ProgressAnalytics.overall_recovery_score(

                payload

            )

        )

        payload[

            "overall_recovery_status"

        ] = (

            ProgressAnalytics.overall_recovery_status(

                score

            )

        )

        return payload

    @staticmethod
    def calculate_recovery_status(
            progress_data: dict
        ) -> str:

            score = (
                ProgressAnalytics.overall_recovery_score(
                    progress_data
                )
            )

            return (
                ProgressAnalytics.overall_recovery_status(
                    score
                )
            )    

    @staticmethod
    def register_progress(

        progress_data: dict

    ) -> dict:

        ProgressService.validate_progress(

            progress_data

        )

        payload = (

            ProgressService.create_progress_payload(

                progress_data

            )

        )

        ProgressCreate(

            **payload

        )

        return payload