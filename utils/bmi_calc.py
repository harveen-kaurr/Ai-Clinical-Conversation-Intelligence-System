def calculate_bmi(
    weight_kg: float,
    height_cm: float
) -> float:
    """
    Calculate BMI using weight (kg)
    and height (cm).
    """

    if weight_kg <= 0:
        raise ValueError(
            "Weight must be greater than zero"
        )

    if height_cm <= 0:
        raise ValueError(
            "Height must be greater than zero"
        )

    if not 50 <= height_cm <= 250:
        raise ValueError(
            "Height outside valid range"
        )

    if not 2 <= weight_kg <= 500:
        raise ValueError(
            "Weight outside valid range"
        )

    height_m = height_cm / 100

    bmi = weight_kg / (height_m ** 2)

    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    """
    Return BMI category.
    """

    if bmi < 18.5:
        return "Underweight"

    if bmi < 25:
        return "Normal"

    if bmi < 30:
        return "Overweight"

    return "Obese"


def bmi_risk(bmi: float) -> str:
    """
    Return health risk level
    associated with BMI.
    """

    if bmi < 18.5:
        return "Increased Risk"

    if bmi < 25:
        return "Average Risk"

    if bmi < 30:
        return "Increased Risk"

    return "High Risk"


def get_bmi_data(
    weight_kg: float,
    height_cm: float
) -> dict:
    """
    Return complete BMI information.
    """

    bmi = calculate_bmi(
        weight_kg=weight_kg,
        height_cm=height_cm
    )

    return {
        "bmi": bmi,
        "category": bmi_category(bmi),
        "risk": bmi_risk(bmi)
    }