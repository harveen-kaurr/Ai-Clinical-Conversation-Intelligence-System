def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Calculate BMI given weight in kilograms and height in centimeters.
    Returns BMI rounded to 1 decimal place.
    """
    if height_cm <= 0:
        raise ValueError("Height must be greater than zero")
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m * height_m)
    return round(bmi, 1)

def bmi_category(bmi: float) -> str:
    """
    Return BMI category based on BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_risk(bmi: float) -> str:
    """
    Return risk level based on BMI.
    """
    if bmi < 18.5:
        return "Increased risk (underweight)"
    elif bmi < 25:
        return "Average risk"
    elif bmi < 30:
        return "Increased risk (overweight)"
    else:
        return "High risk (obese)"
