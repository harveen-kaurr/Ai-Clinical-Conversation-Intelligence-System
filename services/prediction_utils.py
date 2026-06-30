from typing import Dict


class PredictionUtils:

    @staticmethod
    def classify_patient(
        ai_result: dict,
        rule_result: dict
    ) -> Dict:

        gemini_risk = str(
            ai_result.get(
                "risk_level",
                ""
            )
        ).lower()

        rule_risk = str(
            rule_result.get(
                "risk_level",
                ""
            )
        ).lower()

        surgery_probability = float(
            ai_result.get(
                "surgery_probability",
                0
            )
        )

        pain_level = "Mild"

        patient_category = "Routine"

        recovery_priority = "Low"

        therapy_priority = "Normal"

        # -------------------------
        # Pain Classification
        # -------------------------

        if (
            "high" in gemini_risk
            or
            "high" in rule_risk
        ):

            pain_level = "Severe"

        elif (
            "moderate" in gemini_risk
            or
            "medium" in gemini_risk
            or
            "moderate" in rule_risk
            or
            "medium" in rule_risk
        ):

            pain_level = "Moderate"

        else:

            pain_level = "Mild"

        # -------------------------
        # Surgery Prediction
        # -------------------------

        if surgery_probability >= 0.70:

            patient_category = "Critical"

            recovery_priority = "High"

            therapy_priority = "Immediate"

        elif surgery_probability >= 0.40:

            patient_category = "Priority"

            recovery_priority = "Medium"

            therapy_priority = "Early"

        else:

            patient_category = "Routine"

            recovery_priority = "Low"

            therapy_priority = "Normal"

        return {

            "pain_level":
                pain_level,

            "patient_category":
                patient_category,

            "therapy_priority":
                therapy_priority,

            "recovery_priority":
                recovery_priority

        }