from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class TreatmentBase(BaseModel):

    consultation_id: str

    treatment_type: str

    treatment_plan: Optional[str] = None

    medication: Optional[str] = None

    session_number: Optional[int] = None

    session_date: date

    therapist_name: Optional[str] = None

    treatment_status: Optional[str] = None

    followup_required: Optional[bool] = False

    notes: Optional[str] = None


class TreatmentCreate(TreatmentBase):
    pass


class TreatmentUpdate(BaseModel):

    treatment_type: Optional[str] = None

    treatment_plan: Optional[str] = None

    medication: Optional[str] = None

    session_number: Optional[int] = None

    session_date: Optional[date] = None

    therapist_name: Optional[str] = None

    treatment_status: Optional[str] = None

    followup_required: Optional[bool] = None

    notes: Optional[str] = None


class Treatment(TreatmentBase):

    treatment_id: str

    created_at: datetime

    class Config:

        from_attributes = True