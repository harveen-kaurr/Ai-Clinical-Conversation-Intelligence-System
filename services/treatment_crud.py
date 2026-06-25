from database.supabase_client import supabase
from database.database_service import DatabaseService

TABLE_NAME = "treatments"


def create_treatment(
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


def get_all_treatments():

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
    )

    return DatabaseService.execute_query(
        query
    )


def get_treatment_by_id(
    treatment_id: str
):

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
        .eq(
            "treatment_id",
            treatment_id
        )
    )

    result = DatabaseService.execute_query(
        query
    )

    return result[0] if result else None


def update_treatment(
    treatment_id: str,
    updated_data: dict
):

    query = (
        supabase
        .table(TABLE_NAME)
        .update(updated_data)
        .eq(
            "treatment_id",
            treatment_id
        )
    )

    return DatabaseService.execute_query(
        query
    )


def delete_treatment(
    treatment_id: str
):

    query = (
        supabase
        .table(TABLE_NAME)
        .delete()
        .eq(
            "treatment_id",
            treatment_id
        )
    )

    return DatabaseService.execute_query(
        query
    )


def search_treatments(
    consultation_id: str = None,
    treatment_type: str = None
):

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
    )

    if consultation_id:

        query = query.eq(
            "consultation_id",
            consultation_id
        )

    if treatment_type:

        query = query.ilike(
            "treatment_type",
            f"%{treatment_type}%"
        )

    return DatabaseService.execute_query(
        query
    )