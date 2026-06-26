from datetime import datetime
from typing import Optional, Dict, Any

from pydantic import BaseModel


class AIAnalysisBase(BaseModel):

    conversation_id: str

    summary: Optional[str] = None

    extracted_symptoms: Optional[str] = None

    pain_keywords: Optional[str] = None

    emotional_state: Optional[str] = None

    risk_level: Optional[str] = None

    surgery_probability: Optional[float] = None

    recovery_prediction: Optional[str] = None

    ai_confidence: Optional[float] = None

    recommendations: Optional[str] = None

    structured_output: Optional[Dict[str, Any]] = None


class AIAnalysisCreate(AIAnalysisBase):
    pass


class AIAnalysisUpdate(BaseModel):

    summary: Optional[str] = None

    extracted_symptoms: Optional[str] = None

    pain_keywords: Optional[str] = None

    emotional_state: Optional[str] = None

    risk_level: Optional[str] = None

    surgery_probability: Optional[float] = None

    recovery_prediction: Optional[str] = None

    ai_confidence: Optional[float] = None

    recommendations: Optional[str] = None

    structured_output: Optional[Dict[str, Any]] = None


class AIAnalysis(AIAnalysisBase):

    analysis_id: str

    created_at: datetime

    class Config:

        from_attributes = True