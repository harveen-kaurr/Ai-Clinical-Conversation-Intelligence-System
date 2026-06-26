from models.ai_analysis import (
    AIAnalysisCreate
)


class AIService:

    REQUIRED_FIELDS = [

        "conversation_id"

    ]

    @staticmethod
    def validate_analysis(
        analysis_data: dict
    ) -> None:

        for field in AIService.REQUIRED_FIELDS:

            if (
                field not in analysis_data
                or analysis_data[field] is None
                or analysis_data[field] == ""
            ):

                raise ValueError(
                    f"{field} is required"
                )

    @staticmethod
    def create_analysis_payload(
        analysis_data: dict
    ) -> dict:

        payload = analysis_data.copy()

        return payload

    @staticmethod
    def analyze_conversation(
        analysis_data: dict
    ) -> dict:

        AIService.validate_analysis(
            analysis_data
        )

        payload = (
            AIService.create_analysis_payload(
                analysis_data
            )
        )

        AIAnalysisCreate(
            **payload
        )

        return payload