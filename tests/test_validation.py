from utils.validation import (
    validate_phone_number,
    validate_email,
    validate_age
)


def test_valid_phone():

    valid, _ = (
        validate_phone_number(
            "9876543210"
        )
    )

    assert valid is True


def test_invalid_phone():

    valid, _ = (
        validate_phone_number(
            "12345"
        )
    )

    assert valid is False


def test_valid_email():

    valid, _ = (
        validate_email(
            "test@gmail.com"
        )
    )

    assert valid is True


def test_invalid_email():

    valid, _ = (
        validate_email(
            "invalid-email"
        )
    )

    assert valid is False


def test_valid_age():

    valid, _ = validate_age(25)

    assert valid is True


def test_invalid_age():

    valid, _ = validate_age(150)

    assert valid is False