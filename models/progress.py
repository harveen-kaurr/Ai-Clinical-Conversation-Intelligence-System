from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ProgressBase(BaseModel):

    patient_id: UUID

    treatment_id: UUID

    session_number: int = Field(..., ge=1)

    progress_date: date

    previous_pain_score: int = Field(..., ge=0, le=10)

    current_pain_score: int = Field(..., ge=0, le=10)

    mobility_improvement: int = Field(..., ge=0, le=100)

    sleep_quality: int = Field(..., ge=0, le=10)

    numbness_improvement: int = Field(..., ge=0, le=100)

    range_of_motion: int = Field(..., ge=0, le=100)

    patient_feedback: Optional[str] = None

    practitioner_remark: Optional[str] = None

    overall_recovery_status: Optional[str] = None


class ProgressCreate(ProgressBase):
    pass


class ProgressUpdate(BaseModel):

    patient_id: Optional[UUID] = None

    treatment_id: Optional[UUID] = None

    session_number: Optional[int] = Field(None, ge=1)

    progress_date: Optional[date] = None

    previous_pain_score: Optional[int] = Field(None, ge=0, le=10)

    current_pain_score: Optional[int] = Field(None, ge=0, le=10)

    mobility_improvement: Optional[int] = Field(None, ge=0, le=100)

    sleep_quality: Optional[int] = Field(None, ge=0, le=10)

    numbness_improvement: Optional[int] = Field(None, ge=0, le=100)

    range_of_motion: Optional[int] = Field(None, ge=0, le=100)

    patient_feedback: Optional[str] = None

    practitioner_remark: Optional[str] = None

    overall_recovery_status: Optional[str] = None


class Progress(ProgressBase):

    progress_id: UUID

    created_at: datetime

    updated_at: datetime

    class Config:
        from_attributes = True