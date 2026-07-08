import json

from dotenv import load_dotenv
from google import genai

from utils.secrets import get_secret

load_dotenv()

GEMINI_API_KEY = get_secret("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY must be set via .env (local) or Streamlit secrets (deployment)."
    )

client = genai.Client(
    api_key=GEMINI_API_KEY
)


class GeminiService:

    @staticmethod
    def analyze_transcript(
        transcript: str
    ) -> dict:

        prompt = f"""
You are an expert AI clinical assistant specializing in Chiropractic, Manual Osteopathy,
Soft Chiropractic Therapy, Ayurveda and Panchakarma.

Analyze the following doctor-patient conversation carefully.

Your tasks are:

1. Generate a concise clinical summary.
2. Extract all symptoms mentioned.
3. Identify pain-related keywords.
4. Determine the patient's emotional state.
5. Classify the clinical risk level as Low, Medium or High.
6. Estimate surgery probability (0-100).
7. Predict the expected recovery duration.
8. Assign an AI confidence score (0-100).
9. Provide practical treatment recommendations.
10. Return ONLY valid JSON.

Do NOT include:
- Markdown
- Explanations
- Code blocks
- Any text outside the JSON

Return ONLY this JSON structure:

{{
    "summary": "Brief clinical summary",

    "extracted_symptoms": "Comma-separated symptoms",

    "pain_keywords": "Comma-separated pain-related keywords",

    "emotional_state": "Calm, Anxious, Distressed, Hopeful, Fatigued or Neutral",

    "risk_level": "Low, Medium or High",

    "surgery_probability": 0,

    "recovery_prediction": "Estimated recovery duration",

    "ai_confidence": 0,

    "recommendations": "Recommended therapies, tests and lifestyle advice",

    "structured_output":
    {{
        "possible_condition": "",
        "body_area": "",
        "recommended_tests": "",
        "recommended_therapy": ""
    }}
}}

Doctor-Patient Conversation:

{transcript}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:

            result = json.loads(
                text
            )

        except json.JSONDecodeError:

            raise ValueError(
                "Gemini returned an invalid JSON response."
            )

        result["surgery_probability"] = max(
            0,
            min(
                100,
                result.get(
                    "surgery_probability",
                    0
                )
            )
        )

        result["ai_confidence"] = max(
            0,
            min(
                100,
                result.get(
                    "ai_confidence",
                    0
                )
            )
        )

        return result