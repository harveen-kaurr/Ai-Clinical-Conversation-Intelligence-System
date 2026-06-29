import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiService:

    @staticmethod
    def analyze_transcript(
        transcript: str
    ) -> dict:

        prompt = f"""
You are an AI clinical assistant.

Analyze the following doctor-patient conversation.

Return ONLY valid JSON.

Required JSON format:

{{
    "summary": "",
    "extracted_symptoms": "",
    "pain_keywords": "",
    "emotional_state": "",
    "risk_level": "",
    "surgery_probability": 0,
    "recovery_prediction": "",
    "ai_confidence": 0,
    "recommendations": "",
    "structured_output": {{}}
}}

Conversation:

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

        return json.loads(text)