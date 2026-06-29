from models.ai_analysis import (
    AIAnalysisCreate
)

from services.gemini_service import (
    GeminiService
)


class AIService:

    REQUIRED_FIELDS = [

        "conversation_id",

        "transcript"

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

        ai_result = (
            GeminiService.analyze_transcript(
                analysis_data["transcript"]
            )
        )

        payload = {

            "conversation_id":
                analysis_data["conversation_id"],

            "transcript":
                analysis_data["transcript"],    

            "summary":
                ai_result["summary"],

            "extracted_symptoms":
                ai_result["extracted_symptoms"],

            "pain_keywords":
                ai_result["pain_keywords"],

            "emotional_state":
                ai_result["emotional_state"],

            "risk_level":
                ai_result["risk_level"],

            "surgery_probability":
                ai_result["surgery_probability"],

            "recovery_prediction":
                ai_result["recovery_prediction"],

            "ai_confidence":
                ai_result["ai_confidence"],

            "recommendations":
                ai_result["recommendations"],

            "structured_output":
                ai_result["structured_output"]

        }

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