import re
from typing import Tuple

def validate_phone_number(phone: str) -> Tuple[bool, str]:
    """Validate phone number: digits only, length 10-15."""
    if not phone.isdigit():
        return False, "Phone number must contain only digits"
    if not (10 <= len(phone) <= 15):
        return False, "Phone number length must be between 10 and 15 digits"
    return True, ""

def validate_alternate_phone_number(phone: Optional[str]) -> Tuple[bool, str]:
    if phone is None or phone == "":
        return True, ""  # optional field empty is ok
    return validate_phone_number(phone)

def validate_email(email: Optional[str]) -> Tuple[bool, str]:
    if email is None or email == "":
        return True, ""  # optional
    pattern = r'^[\w\.-]+@[\w\.-]+\.[\w]+$'
    if re.match(pattern, email):
        return True, ""
    return False, "Invalid email format"

def validate_age(age: int) -> Tuple[bool, str]:
    if 0 <= age <= 120:
        return True, ""
    return False, "Age must be between 0 and 120"

def validate_required_fields(data: dict, required: list) -> Tuple[bool, str]:
    missing = [field for field in required if not data.get(field)]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    return True, ""

def validate_gender(gender: str) -> Tuple[bool, str]:
    if gender in ("Male", "Female", "Other"):
        return True, ""
    return False, "Gender must be Male, Female, or Other"

def validate_duplicate_patient(supabase, phone_number: str, exclude_id: Optional[str] = None) -> Tuple[bool, str]:
    """Check if a patient with the same phone number already exists."""
    try:
        query = supabase.table("patients").select("id").eq("phone_number", phone_number)
        if exclude_id:
            query = query.neq("id", exclude_id)
        response = query.execute()
        if response.data and len(response.data) > 0:
            return False, "A patient with this phone number already exists"
        return True, ""
    except Exception as e:
        return False, f"Error checking duplicate: {str(e)}"

# Note: You may add more validation functions as needed.
