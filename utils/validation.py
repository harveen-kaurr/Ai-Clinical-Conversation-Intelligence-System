import re
from typing import Optional, Tuple


def validate_phone_number(
    phone: str
) -> Tuple[bool, str]:

    if not re.match(
        r"^[6-9]\d{9}$",
        phone
    ):
        return (
            False,
            "Invalid phone number"
        )

    return True, ""


def validate_alternate_phone_number(
    phone: Optional[str]
) -> Tuple[bool, str]:

    if not phone:
        return True, ""

    return validate_phone_number(phone)


def validate_email(
    email: Optional[str]
) -> Tuple[bool, str]:

    if not email:
        return True, ""

    pattern = (
        r"^[\w\.-]+"
        r"@[\w\.-]+"
        r"\.[\w]+$"
    )

    if re.match(pattern, email):
        return True, ""

    return (
        False,
        "Invalid email format"
    )


def validate_age(
    age: int
) -> Tuple[bool, str]:

    if 0 <= age <= 120:
        return True, ""

    return (
        False,
        "Age must be between 0 and 120"
    )


def validate_emergency_contact(
    contact: Optional[str]
) -> Tuple[bool, str]:

    if not contact:
        return True, ""

    return validate_phone_number(contact)


def validate_gender(
    gender: str
) -> Tuple[bool, str]:

    valid_values = (
        "Male",
        "Female",
        "Other"
    )

    if gender in valid_values:
        return True, ""

    return (
        False,
        "Invalid gender"
    )


def validate_required_fields(
    data: dict,
    required_fields: list
) -> Tuple[bool, str]:

    missing_fields = []

    for field in required_fields:

        if field not in data:
            missing_fields.append(field)

        elif data[field] is None:
            missing_fields.append(field)

        elif str(data[field]).strip() == "":
            missing_fields.append(field)

    if missing_fields:

        return (
            False,
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    return True, ""


def validate_duplicate_patient(
    supabase,
    phone_number: str,
    exclude_id: Optional[str] = None
) -> Tuple[bool, str]:

    try:

        query = (
            supabase
            .table("patients")
            .select("patient_id")
            .eq(
                "phone_number",
                phone_number
            )
        )

        if exclude_id:

            query = query.neq(
                "patient_id",
                exclude_id
            )

        response = query.execute()

        if response.data:

            return (
                False,
                "Patient already exists"
            )

        return True, ""

    except Exception as exc:

        return (
            False,
            f"Duplicate check failed: {exc}"
        )