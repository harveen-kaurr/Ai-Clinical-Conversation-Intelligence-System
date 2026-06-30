from models.ai_analysis import (
    AIAnalysisCreate
)

from services.gemini_service import (
    GeminiService
)

from services.clinical_rules import (
    ClinicalRules
)
from services.prediction_utils import (
    PredictionUtils
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

        rule_result = (
            ClinicalRules.evaluate(
                analysis_data
            )
        )
        prediction_result = (
            PredictionUtils.classify_patient(
                ai_result,
                rule_result
            )
        )

        recommendations = (
        ai_result.get(
            "recommendations",
            ""
        )
    )

        structured_output = (
            ai_result.get(
                "structured_output",
                {}
            )
        )

        structured_output["clinical_rules"] = {
            "rule_risk_level": rule_result["risk_level"],
            "rule_surgery_probability": rule_result["surgery_probability"],
            "rule_recovery_prediction": rule_result["recovery_prediction"],
            "recommended_therapy": rule_result["recommendations"],
            "follow_up": rule_result["follow_up"],
            "suggested_tests": rule_result["suggested_tests"],
            "flags": rule_result["flags"]
        }

        structured_output["prediction_engine"] = {
            "pain_level": prediction_result["pain_level"],
            "patient_category": prediction_result["patient_category"],
            "therapy_priority": prediction_result["therapy_priority"],
            "recovery_priority": prediction_result["recovery_priority"]
        }

        payload = {

            "conversation_id":
                analysis_data["conversation_id"],

            "transcript":
                analysis_data["transcript"],

            "summary":
                ai_result["summary"],

            "extracted_symptoms":
                (
                        ", ".join(
                            ai_result["extracted_symptoms"]
                        )
                        if isinstance(
                            ai_result.get(
                                "extracted_symptoms"
                            ),
                            list
                        )
                        else ai_result.get(
                            "extracted_symptoms",
                            ""
                        )
                    ),
            "pain_keywords":
                (
        ", ".join(
            ai_result["pain_keywords"]
        )
        if isinstance(
            ai_result.get(
                "pain_keywords"
            ),
            list
        )
        else ai_result.get(
            "pain_keywords",
            ""
        )
    ),

            "emotional_state":
                ai_result["emotional_state"],

            "risk_level":
                ai_result.get(
                    "risk_level"
                )
                or
                rule_result["risk_level"],

            "surgery_probability":
                ai_result.get(
                    "surgery_probability"
                )
                or
                rule_result["surgery_probability"],

            "recovery_prediction":
                ai_result.get(
                    "recovery_prediction"
                )
                or
                rule_result["recovery_prediction"],

            "ai_confidence":
                ai_result["ai_confidence"],

            "recommendations":
                recommendations,

            "structured_output":
                structured_output

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