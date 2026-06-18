from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class PatientBase(BaseModel):
    patient_name: str = Field(..., min_length=1, max_length=100)
    gender: str = Field(..., pattern='^(Male|Female|Other)$')
    email: Optional[str] = Field(None, pattern='^[\w\.-]+@[\w\.-]+\.[\w]+$')
    age: int = Field(..., ge=0, le=120)
    address: Optional[str] = Field(None, max_length=200)
    phone_number: str = Field(..., pattern='^\d{10,15}$')
    alternate_phone_number: Optional[str] = Field(None, pattern='^\d{10,15}$')
    date_of_birth: Optional[str] = Field(None)
    date_of_visiting: Optional[str] = Field(None)
    occupation: Optional[str] = Field(None, max_length=100)
    disease: Optional[str] = Field(None, max_length=100)
    disease_category: Optional[str] = Field(None, max_length=100)

    @validator('phone_number')
    def validate_phone(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits')
        return v

    @validator('alternate_phone_number')
    def validate_alt_phone(cls, v):
        if v is not None and not v.isdigit():
            raise ValueError('Alternate phone number must contain only digits')
        return v

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    patient_name: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    alternate_phone_number: Optional[str] = None
    date_of_birth: Optional[str] = None
    date_of_visiting: Optional[str] = None
    occupation: Optional[str] = None
    disease: Optional[str] = None
    disease_category: Optional[str] = None

class PatientInDB(PatientBase):
    id: str
    created_at: datetime
    updated_at: datetime
