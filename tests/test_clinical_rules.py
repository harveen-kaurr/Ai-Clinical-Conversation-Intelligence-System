import unittest

from services.clinical_rules import ClinicalRules


class TestClinicalRules(unittest.TestCase):

    def test_severe_case(self):

        transcript = (
            "Patient has severe lower back pain, "
            "difficulty walking, sciatica, slip disc, "
            "numbness and stress."
        )

        result = ClinicalRules.evaluate(
            {
                "transcript": transcript
            }
        )

        self.assertEqual(
            result["risk_level"],
            "High"
        )

        self.assertEqual(
            result["follow_up"],
            "3 Days"
        )

        self.assertIn(
            "Possible Slip Disc",
            result["flags"]
        )

        self.assertIn(
            "Neurological Symptoms",
            result["flags"]
        )

    def test_low_risk(self):

        transcript = (
            "Patient has mild neck stiffness."
        )

        result = ClinicalRules.evaluate(
            {
                "transcript": transcript
            }
        )

        self.assertEqual(
            result["risk_level"],
            "Low"
        )

        self.assertEqual(
            result["follow_up"],
            "30 Days"
        )


if __name__ == "__main__":
    unittest.main()