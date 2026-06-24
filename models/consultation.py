from pydantic import BaseModel
from typing import Optional
from datetime import date, time, datetime


class ConsultationBase(BaseModel):
    patient_id: str

    doctor_name: str
    specialization: str

    consultation_date: date
    consultation_time: time

    chief_complaint: str

    clinical_findings: Optional[str] = None

    spine_exam: Optional[str] = None
    muscle_exam: Optional[str] = None
    nerve_exam: Optional[str] = None
    tissue_exam: Optional[str] = None
    bone_joint_exam: Optional[str] = None

    preliminary_diagnosis: Optional[str] = None
    recommended_scan: Optional[str] = None

    followup_date: Optional[date] = None


class ConsultationCreate(ConsultationBase):
    pass


class ConsultationUpdate(BaseModel):
    doctor_name: Optional[str] = None
    specialization: Optional[str] = None

    consultation_date: Optional[date] = None
    consultation_time: Optional[time] = None

    chief_complaint: Optional[str] = None

    clinical_findings: Optional[str] = None

    spine_exam: Optional[str] = None
    muscle_exam: Optional[str] = None
    nerve_exam: Optional[str] = None
    tissue_exam: Optional[str] = None
    bone_joint_exam: Optional[str] = None

    preliminary_diagnosis: Optional[str] = None
    recommended_scan: Optional[str] = None

    followup_date: Optional[date] = None


class Consultation(ConsultationBase):
    consultation_id: str
    created_at: datetime

    class Config:
        from_attributes = True