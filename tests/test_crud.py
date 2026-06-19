from services.patient_crud import (
    get_all_patients,
    get_patient_by_id,
    create_patient,
    update_patient,
    delete_patient
)

# READ ALL
patients = get_all_patients()
print("Total patients:", len(patients))

# CREATE
new_patient = {
    "patient_name": "Test Patient",
    "gender": "Female",
    "age": 25,
    "phone_number": "9999999999"
}

created = create_patient(new_patient)
print("Created:", created)

# Get generated UUID
patient_id = created[0]["patient_id"]

# READ BY ID
patient = get_patient_by_id(patient_id)
print("Patient:", patient)

# UPDATE
updated = update_patient(
    patient_id,
    {
        "age": 30
    }
)
print("Updated:", updated)

# DELETE
deleted = delete_patient(patient_id)
print("Deleted:", deleted)