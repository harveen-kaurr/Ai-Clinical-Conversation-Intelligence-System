from database.supabase_client import supabase
from database.database_service import DatabaseService

TABLE_NAME = "progress_tracking"


def create_progress(
    data: dict
):

    query = (
        supabase
        .table(TABLE_NAME)
        .insert(data)
    )

    return DatabaseService.execute_query(
        query
    )


def get_all_progress():

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
        .order(
            "progress_date",
            desc=True
        )
    )

    return DatabaseService.execute_query(
        query
    )


def get_progress_by_id(
    progress_id: str
):

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
        .eq(
            "progress_id",
            progress_id
        )
    )

    result = DatabaseService.execute_query(
        query
    )

    return result[0] if result else None


def update_progress(
    progress_id: str,
    updated_data: dict
):

    query = (
        supabase
        .table(TABLE_NAME)
        .update(updated_data)
        .eq(
            "progress_id",
            progress_id
        )
    )

    return DatabaseService.execute_query(
        query
    )


def delete_progress(
    progress_id: str
):

    query = (
        supabase
        .table(TABLE_NAME)
        .delete()
        .eq(
            "progress_id",
            progress_id
        )
    )

    return DatabaseService.execute_query(
        query
    )


def search_progress(
    patient_id: str = None,
    treatment_id: str = None,
    session_number: int = None
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

    if treatment_id:

        query = query.eq(
            "treatment_id",
            treatment_id
        )

    if session_number:

        query = query.eq(
            "session_number",
            session_number
        )

    return DatabaseService.execute_query(
        query
    )