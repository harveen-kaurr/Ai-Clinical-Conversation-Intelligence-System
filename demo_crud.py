from services.patient_crud import (
    get_all_patients,
    get_patient_by_id,
    create_patient,
    update_patient,
    delete_patient,
    search_patient_by_name,
    search_patient_by_phone,
    search_patient_by_patient_id
)

# READ ALL
patients = get_all_patients()

print("\n===== READ ALL =====")
print(f"Total Patients: {len(patients)}")

# CREATE
new_patient = {
    "patient_name": "Test Patient",
    "gender": "Female",
    "age": 25,
    "phone_number": "9999999999"
}

created = create_patient(new_patient)

print("\n===== CREATE =====")
print(f"Patient ID: {created[0]['patient_id']}")
print(f"Name: {created[0]['patient_name']}")
print(f"Age: {created[0]['age']}")

# GET GENERATED PATIENT ID
patient_id = created[0]["patient_id"]

# READ BY ID
patient = get_patient_by_id(patient_id)

print("\n===== READ BY ID =====")
print(f"Name: {patient[0]['patient_name']}")
print(f"Phone: {patient[0]['phone_number']}")
print(f"Age: {patient[0]['age']}")

# UPDATE
updated = update_patient(
    patient_id,
    {
        "age": 30
    }
)

print("\n===== UPDATE =====")
print(f"Updated Age: {updated[0]['age']}")

# SEARCH BY PATIENT ID
print("\n===== SEARCH BY PATIENT ID =====")

result = search_patient_by_patient_id(patient_id)

if result:
    print(
        f"{result[0]['patient_name']} - "
        f"{result[0]['patient_id']}"
    )

# SEARCH BY NAME
print("\n===== SEARCH BY NAME =====")

results = search_patient_by_name("Raj")

for patient in results:
    print(
        f"{patient['patient_name']} - "
        f"{patient['phone_number']}"
    )

# SEARCH BY PHONE NUMBER
print("\n===== SEARCH BY PHONE NUMBER =====")

results = search_patient_by_phone("9999999999")

for patient in results:
    print(
        f"{patient['patient_name']} - "
        f"{patient['phone_number']}"
    )

# DELETE
deleted = delete_patient(patient_id)

print("\n===== DELETE =====")
print(f"Deleted Patient: {deleted[0]['patient_name']}")