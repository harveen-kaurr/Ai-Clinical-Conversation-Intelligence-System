from Database.supabase_client import supabase
from Database.database_service import DatabaseService


#Read all Patient
def get_all_patients():
    query = (
        supabase
        .table("patients")
        .select("*")
    )

    return DatabaseService.execute_query(query)

#Read all patient by id
def get_patient_by_id(patient_id):

    query = (
        supabase
        .table("patients")
        .select("*")
        .eq("patient_id", patient_id)
    )

    return DatabaseService.execute_query(query)

#Create new patient
def create_patient(patient_data):

    query = (
        supabase
        .table("patients")
        .insert(patient_data)
    )

    return DatabaseService.execute_query(query)

#Update existing patient
def update_patient(patient_id, updated_data):

    query = (
        supabase
        .table("patients")
        .update(updated_data)
        .eq("patient_id", patient_id)
    )

    return DatabaseService.execute_query(query)

#Delete patient
def delete_patient(patient_id):

    query = (
        supabase
        .table("patients")
        .delete()
        .eq("patient_id", patient_id)
    )

    return DatabaseService.execute_query(query)

#Search patient by name
def search_patient_by_name(name):

    query = (
        supabase
        .table("patients")
        .select("*")
        .ilike(
            "patient_name",
            f"%{name}%"
        )
    )

    return DatabaseService.execute_query(query)

#Search patient by phone number
def search_patient_by_phone(phone_number):

    query = (
        supabase
        .table("patients")
        .select("*")
        .eq(
            "phone_number",
            phone_number
        )
    )

    return DatabaseService.execute_query(query)

# Search patient by patient id
def search_patient_by_patient_id(patient_id):

    query = (
        supabase
        .table("patients")
        .select("*")
        .eq(
            "patient_id",
            patient_id
        )
    )

    return DatabaseService.execute_query(query)