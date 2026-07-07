from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ConversationBase(BaseModel):
    consultation_id: str

    source: str

    # Optional for manual transcript entries
    audio_file_url: Optional[str] = None

    raw_transcript: Optional[str] = None

    language: Optional[str] = None

    speaker_separation: Optional[str] = None

    emotional_state: Optional[str] = None

    pain_keywords: Optional[str] = None

    additional_notes: Optional[str] = None


class ConversationCreate(ConversationBase):
    pass


class ConversationUpdate(BaseModel):
    source: Optional[str] = None

    audio_file_url: Optional[str] = None

    raw_transcript: Optional[str] = None

    language: Optional[str] = None

    speaker_separation: Optional[str] = None

    emotional_state: Optional[str] = None

    pain_keywords: Optional[str] = None

    additional_notes: Optional[str] = None


class Conversation(ConversationBase):
    conversation_id: str

    created_at: datetime

    class Config:
        from_attributes = True