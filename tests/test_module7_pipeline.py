import unittest

from services.clinical_rules import ClinicalRules
from services.prediction_utils import PredictionUtils


class TestModule7Pipeline(unittest.TestCase):

    def test_complete_pipeline(self):

        transcript = (
            "Patient has severe pain, "
            "slip disc and numbness."
        )

        rules = ClinicalRules.evaluate(
            {
                "transcript": transcript
            }
        )

        ai = {
            "risk_level": "High",
            "surgery_probability": 0.80
        }

        prediction = (
            PredictionUtils.classify_patient(
                ai,
                rules
            )
        )

        self.assertEqual(
            prediction["patient_category"],
            "Critical"
        )

        self.assertEqual(
            prediction["pain_level"],
            "Severe"
        )


if __name__ == "__main__":
    unittest.main()