from database.supabase_client import supabase
from database.database_service import DatabaseService

TABLE_NAME = "consultations"


def create_consultation(data: dict):
    query = (
        supabase
        .table(TABLE_NAME)
        .insert(data)
    )

    return DatabaseService.execute_query(query)


def get_all_consultations():
    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
    )

    return DatabaseService.execute_query(query)


def get_consultation_by_id(consultation_id: str):
    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
        .eq("consultation_id", consultation_id)
    )

    result = DatabaseService.execute_query(query)

    return result[0] if result else None


def update_consultation(
    consultation_id: str,
    updated_data: dict
):
    query = (
        supabase
        .table(TABLE_NAME)
        .update(updated_data)
        .eq("consultation_id", consultation_id)
    )

    return DatabaseService.execute_query(query)


def delete_consultation(
    consultation_id: str
):
    query = (
        supabase
        .table(TABLE_NAME)
        .delete()
        .eq("consultation_id", consultation_id)
    )

    return DatabaseService.execute_query(query)


def search_consultations(
    patient_id: str = None,
    doctor_name: str = None
):
    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
    )

    if patient_id:
        query = query.eq(
            "patient_id",
            patient_id
        )

    if doctor_name:
        query = query.ilike(
            "doctor_name",
            f"%{doctor_name}%"
        )

    return DatabaseService.execute_query(query)