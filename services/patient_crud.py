from Database.supabase_client import supabase

def get_all_patients():
    response = (
        supabase
        .table("patients")
        .select("*")
        .execute()
    )
    return response.data

def get_patient_by_id(patient_id):
    response = (
        supabase
        .table("patients")
        .select("*")
        .eq("patient_id", patient_id)
        .execute()
    )
    return response.data

def create_patient(patient_data):
    response = (
        supabase
        .table("patients")
        .insert(patient_data)
        .execute()
    )

    return response.data

def update_patient(patient_id, updated_data):
    response = (
        supabase
        .table("patients")
        .update(updated_data)
        .eq("patient_id", patient_id)
        .execute()
    )

    return response.data

def delete_patient(patient_id):
    response = (
        supabase
        .table("patients")
        .delete()
        .eq("patient_id", patient_id)
        .execute()
    )

    return response.data