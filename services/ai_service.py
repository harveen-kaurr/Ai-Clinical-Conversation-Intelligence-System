from models.ai_analysis import (
    AIAnalysisCreate
)

from services.whisper_service import (
    WhisperService
)


class AIService:

    REQUIRED_FIELDS = [

        "conversation_id",

        "audio_url"

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

        whisper_service = (
            WhisperService()
        )

        transcript = (
            whisper_service.transcribe_audio(
                analysis_data["audio_url"]
            )
        )

        payload = {

            "conversation_id":
                analysis_data["conversation_id"],

            "transcript":
                transcript,

            "summary":
                None,

            "extracted_symptoms":
                None,

            "pain_keywords":
                None,

            "emotional_state":
                None,

            "risk_level":
                None,

            "surgery_probability":
                None,

            "recovery_prediction":
                None,

            "ai_confidence":
                None,

            "recommendations":
                None,

            "structured_output":
                None

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