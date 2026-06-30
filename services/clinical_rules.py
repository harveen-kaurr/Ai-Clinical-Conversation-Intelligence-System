import re


class ClinicalRules:

    @staticmethod
    def evaluate(
        analysis_data: dict
    ) -> dict:

        transcript = (
            analysis_data.get(
                "transcript",
                ""
            ).lower()
        )

        risk_level = "Low"

        follow_up = "30 Days"

        suggested_tests = []

        recommendations = []

        flags = []

        surgery_probability = 10

        recovery_prediction = (
            "Recovery expected within 4-6 weeks"
        )

        # -----------------------------
        # Pain Score Detection
        # -----------------------------

        pain_match = re.search(
            r'(\d+)\s*/\s*10',
            transcript
        )

        if pain_match:

            score = int(
                pain_match.group(1)
            )

            if score >= 8:

                risk_level = "High"

                follow_up = "3 Days"

                surgery_probability = 80

                recovery_prediction = (
                    "Recovery may require intensive treatment"
                )

                flags.append(
                    "Severe Pain"
                )

            elif score >= 5:

                risk_level = "Medium"

                follow_up = "7 Days"

                surgery_probability = 40

                recovery_prediction = (
                    "Recovery expected within 2-4 weeks"
                )

                flags.append(
                    "Moderate Pain"
                )

        # -----------------------------
        # Severe Pain Keywords
        # -----------------------------

        severe_words = [

            "severe",

            "unbearable",

            "cannot walk",

            "can't walk",

            "unable to walk",

            "difficulty walking",

            "difficulty standing",

            "prolonged standing"

        ]

        if any(
            word in transcript
            for word in severe_words
        ):

            risk_level = "High"

            follow_up = "3 Days"

            surgery_probability = max(
                surgery_probability,
                80
            )

            recovery_prediction = (
                "Recovery may require intensive treatment"
            )

            if (
                "Severe Pain"
                not in flags
            ):

                flags.append(
                    "Severe Pain"
                )

        # -----------------------------
        # Slip Disc
        # -----------------------------

        if (
            "slip disc" in transcript
            or
            "disc bulge" in transcript
        ):

            recommendations.append(
                "Chiropractic Therapy"
            )

            suggested_tests.append(
                "MRI Lumbosacral Spine"
            )

            flags.append(
                "Possible Slip Disc"
            )

        # -----------------------------
        # Sciatica
        # -----------------------------

        if (
            "sciatica" in transcript
            or
            "radiating pain" in transcript
            or
            "radiates" in transcript
        ):

            recommendations.extend(

                [

                    "Soft Tissue Therapy",

                    "Nerve Mobilization"

                ]

            )

            suggested_tests.append(
                "MRI Lumbosacral Spine"
            )

        # -----------------------------
        # Numbness
        # -----------------------------

        if (
            "numbness" in transcript
            or
            "tingling" in transcript
        ):

            suggested_tests.append(
                "Neurological Examination"
            )

            flags.append(
                "Neurological Symptoms"
            )

        # -----------------------------
        # Weakness
        # -----------------------------

        if "weakness" in transcript:

            suggested_tests.append(
                "Muscle Strength Assessment"
            )

        # -----------------------------
        # Diabetes
        # -----------------------------

        if "diabetes" in transcript:

            suggested_tests.append(
                "HbA1c"
            )

            recommendations.append(
                "Lifestyle Modification"
            )

        # -----------------------------
        # Stress
        # -----------------------------

        if (
            "stress" in transcript
            or
            "anxiety" in transcript
        ):

            recommendations.extend(

                [

                    "Breathing Exercises",

                    "Meditation"

                ]

            )

        recommendations = list(
            dict.fromkeys(
                recommendations
            )
        )

        suggested_tests = list(
            dict.fromkeys(
                suggested_tests
            )
        )

        flags = list(
            dict.fromkeys(
                flags
            )
        )

        return {

            "risk_level":
                risk_level,

            "follow_up":
                follow_up,

            "suggested_tests":
                suggested_tests,

            "recommendations":
                recommendations,

            "flags":
                flags,

            "surgery_probability":
                surgery_probability,

            "recovery_prediction":
                recovery_prediction

        }