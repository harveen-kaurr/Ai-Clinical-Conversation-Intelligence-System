from database.supabase_client import supabase
from database.database_service import DatabaseService

TABLE_NAME = "ai_analysis"


def create_analysis(
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


def get_all_analysis():

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
    )

    return DatabaseService.execute_query(
        query
    )


def get_analysis_by_id(
    analysis_id: str
):

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
        .eq(
            "analysis_id",
            analysis_id
        )
    )

    result = DatabaseService.execute_query(
        query
    )

    return result[0] if result else None


def update_analysis(
    analysis_id: str,
    updated_data: dict
):

    query = (
        supabase
        .table(TABLE_NAME)
        .update(updated_data)
        .eq(
            "analysis_id",
            analysis_id
        )
    )

    return DatabaseService.execute_query(
        query
    )


def delete_analysis(
    analysis_id: str
):

    query = (
        supabase
        .table(TABLE_NAME)
        .delete()
        .eq(
            "analysis_id",
            analysis_id
        )
    )

    return DatabaseService.execute_query(
        query
    )


def get_analysis_by_conversation(
    conversation_id: str
):

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
        .eq(
            "conversation_id",
            conversation_id
        )
    )

    return DatabaseService.execute_query(
        query
    )