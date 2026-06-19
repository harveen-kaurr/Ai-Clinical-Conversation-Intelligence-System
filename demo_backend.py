from services.patient_service import PatientService

patient_data = {
    "patient_name": "Demo Patient",
    "gender": "Male",
    "age": 30,
    "phone_number": "9876543210",
    "height_cm": 175,
    "weight_kg": 70
}

result = PatientService.register_patient(
    patient_data=patient_data,
    sequence=1
)

print(f"Patient ID     : {result['patient_id']}")
print(f"Patient Name   : {result['patient_name']}")
print(f"Gender         : {result['gender']}")
print(f"Age            : {result['age']}")
print(f"Phone Number   : {result['phone_number']}")
print(f"Height (cm)    : {result['height_cm']}")
print(f"Weight (kg)    : {result['weight_kg']}")
print(f"BMI            : {result['bmi']}")
print(f"BMI Category   : {result['bmi_category']}")