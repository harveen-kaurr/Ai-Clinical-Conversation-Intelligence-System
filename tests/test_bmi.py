from utils.bmi_calc import (
    calculate_bmi,
    bmi_category
)


def test_bmi_calculation():

    bmi = calculate_bmi(
        weight_kg=70,
        height_cm=170
    )

    assert bmi == 24.22


def test_underweight_category():

    assert (
        bmi_category(17)
        == "Underweight"
    )


def test_normal_category():

    assert (
        bmi_category(22)
        == "Normal"
    )


def test_overweight_category():

    assert (
        bmi_category(28)
        == "Overweight"
    )


def test_obese_category():

    assert (
        bmi_category(35)
        == "Obese"
    )