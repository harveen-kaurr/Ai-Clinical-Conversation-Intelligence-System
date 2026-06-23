from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class PatientBase(BaseModel):
    patient_name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    patient_id: Optional[str] = None
    gender: str = Field(
        ...,
        pattern=r"^(Male|Female|Other)$"
    )

    age: int = Field(
        ...,
        ge=0,
        le=120
    )

    phone_number: str = Field(
        ...,
        pattern=r"^[6-9]\d{9}$"
    )

    alternate_phone_number: Optional[str] = Field(
        None,
        pattern=r"^[6-9]\d{9}$"
    )

    email: Optional[str] = Field(
        None,
        pattern=r"^[\w\.-]+@[\w\.-]+\.[\w]+$"
    )

    address: Optional[str] = Field(
        None,
        max_length=250
    )

    date_of_birth: Optional[str] = None

    date_of_visiting: Optional[str] = None

    occupation: Optional[str] = Field(
        None,
        max_length=100
    )

    disease: Optional[str] = Field(
        None,
        max_length=200
    )

    disease_category: Optional[str] = Field(
        None,
        max_length=100
    )

    height_cm: Optional[float] = Field(
        None,
        gt=0
    )

    weight_kg: Optional[float] = Field(
        None,
        gt=0
    )

    bmi: Optional[float] = None

    bmi_category: Optional[str] = None

    emergency_contact: Optional[str] = Field(
        None,
        pattern=r"^[6-9]\d{9}$"
    )

    lifestyle: Optional[str] = Field(
        None,
        max_length=100
    )

    smoking_alcohol: Optional[str] = Field(
        None,
        max_length=100
    )

    previous_spine_injury: Optional[str] = Field(
        None,
        max_length=250
    )


class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    patient_name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None

    phone_number: Optional[str] = None
    alternate_phone_number: Optional[str] = None

    email: Optional[str] = None
    address: Optional[str] = None

    date_of_birth: Optional[str] = None
    date_of_visiting: Optional[str] = None

    occupation: Optional[str] = None

    disease: Optional[str] = None
    disease_category: Optional[str] = None

    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None

    bmi: Optional[float] = None
    bmi_category: Optional[str] = None

    emergency_contact: Optional[str] = None

    lifestyle: Optional[str] = None

    smoking_alcohol: Optional[str] = None

    previous_spine_injury: Optional[str] = None


class PatientInDB(PatientBase):
    id: str

    patient_id: str

    created_at: datetime

    updated_at: datetime