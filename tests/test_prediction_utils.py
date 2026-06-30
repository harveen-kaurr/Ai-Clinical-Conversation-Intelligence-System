import unittest

from services.prediction_utils import PredictionUtils


class TestPredictionUtils(unittest.TestCase):

    def test_critical_patient(self):

        ai = {
            "risk_level": "High",
            "surgery_probability": 0.85
        }

        rules = {
            "risk_level": "High"
        }

        result = PredictionUtils.classify_patient(
            ai,
            rules
        )

        self.assertEqual(
            result["pain_level"],
            "Severe"
        )

        self.assertEqual(
            result["patient_category"],
            "Critical"
        )

        self.assertEqual(
            result["therapy_priority"],
            "Immediate"
        )

        self.assertEqual(
            result["recovery_priority"],
            "High"
        )

    def test_priority_patient(self):

        ai = {
            "risk_level": "Moderate",
            "surgery_probability": 0.5
        }

        rules = {
            "risk_level": "Medium"
        }

        result = PredictionUtils.classify_patient(
            ai,
            rules
        )

        self.assertEqual(
            result["pain_level"],
            "Moderate"
        )

        self.assertEqual(
            result["patient_category"],
            "Priority"
        )

    def test_routine_patient(self):

        ai = {
            "risk_level": "Low",
            "surgery_probability": 0.1
        }

        rules = {
            "risk_level": "Low"
        }

        result = PredictionUtils.classify_patient(
            ai,
            rules
        )

        self.assertEqual(
            result["patient_category"],
            "Routine"
        )


if __name__ == "__main__":
    unittest.main()