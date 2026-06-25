from database.supabase_client import supabase
from database.database_service import DatabaseService

TABLE_NAME = "conversations"


def create_conversation(data: dict):

    query = (
        supabase
        .table(TABLE_NAME)
        .insert(data)
    )

    return DatabaseService.execute_query(query)


def get_all_conversations():

    query = (
        supabase
        .table(TABLE_NAME)
        .select("*")
    )

    return DatabaseService.execute_query(query)


def get_conversation_by_id(
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

    result = DatabaseService.execute_query(query)

    return result[0] if result else None


def update_conversation(
    conversation_id: str,
    updated_data: dict
):

    query = (
        supabase
        .table(TABLE_NAME)
        .update(updated_data)
        .eq(
            "conversation_id",
            conversation_id
        )
    )

    return DatabaseService.execute_query(query)


def delete_conversation(
    conversation_id: str
):

    query = (
        supabase
        .table(TABLE_NAME)
        .delete()
        .eq(
            "conversation_id",
            conversation_id
        )
    )

    return DatabaseService.execute_query(query)


def search_conversations(
    consultation_id: str = None,
    language: str = None
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

    if language:

        query = query.ilike(
            "language",
            f"%{language}%"
        )

    return DatabaseService.execute_query(query)