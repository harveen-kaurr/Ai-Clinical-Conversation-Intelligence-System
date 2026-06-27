class ProgressAnalytics:

    @staticmethod
    def calculate_pain_improvement(
        previous_pain: int,
        current_pain: int
    ) -> float:

        if previous_pain == 0:
            return 100.0

        improvement = (
            (
                previous_pain -
                current_pain
            ) / previous_pain
        ) * 100

        return round(improvement, 2)

    @staticmethod
    def mobility_status(
        mobility: int
    ) -> str:

        if mobility >= 80:
            return "Excellent"

        elif mobility >= 60:
            return "Good"

        elif mobility >= 40:
            return "Moderate"

        elif mobility >= 20:
            return "Poor"

        return "Critical"

    @staticmethod
    def sleep_status(
        sleep_quality: int
    ) -> str:

        if sleep_quality >= 8:
            return "Excellent"

        elif sleep_quality >= 6:
            return "Good"

        elif sleep_quality >= 4:
            return "Moderate"

        elif sleep_quality >= 2:
            return "Poor"

        return "Critical"

    @staticmethod
    def numbness_status(
        numbness: int
    ) -> str:

        if numbness >= 80:
            return "Excellent"

        elif numbness >= 60:
            return "Good"

        elif numbness >= 40:
            return "Moderate"

        elif numbness >= 20:
            return "Poor"

        return "Critical"

    @staticmethod
    def rom_status(
        rom: int
    ) -> str:

        if rom >= 80:
            return "Excellent"

        elif rom >= 60:
            return "Good"

        elif rom >= 40:
            return "Moderate"

        elif rom >= 20:
            return "Poor"

        return "Critical"

    @staticmethod
    def overall_recovery_score(
        progress_data: dict
    ) -> float:

        pain = ProgressAnalytics.calculate_pain_improvement(

            progress_data["previous_pain_score"],

            progress_data["current_pain_score"]

        )

        mobility = progress_data.get(
            "mobility_improvement",
            0
        )

        sleep = (
            progress_data.get(
                "sleep_quality",
                0
            ) * 10
        )

        numbness = progress_data.get(
            "numbness_improvement",
            0
        )

        rom = progress_data.get(
            "range_of_motion",
            0
        )

        score = (

            pain +

            mobility +

            sleep +

            numbness +

            rom

        ) / 5

        return round(score, 2)

    @staticmethod
    def overall_recovery_status(
        score: float
    ) -> str:

        if score >= 80:
            return "Excellent"

        elif score >= 60:
            return "Good"

        elif score >= 40:
            return "Moderate"

        elif score >= 20:
            return "Poor"

        return "Critical"