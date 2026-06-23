from database.supabase_client import supabase
from database.database_service import DatabaseService

def get_all_assessments():

    query = (
        supabase
        .table("pain_assessments")
        .select("*")
    )

    return DatabaseService.execute_query(query)


def get_assessment_by_id(assessment_id):

    query = (
        supabase
        .table("pain_assessments")
        .select("*")
        .eq("assessment_id", assessment_id)
    )

    return DatabaseService.execute_query(query)


def create_assessment(assessment_data):

    query = (
        supabase
        .table("pain_assessments")
        .insert(assessment_data)
    )

    return DatabaseService.execute_query(query)


def update_assessment(assessment_id, updated_data):

    query = (
        supabase
        .table("pain_assessments")
        .update(updated_data)
        .eq("assessment_id", assessment_id)
    )

    return DatabaseService.execute_query(query)


def delete_assessment(assessment_id):

    query = (
        supabase
        .table("pain_assessments")
        .delete()
        .eq("assessment_id", assessment_id)
    )

    return DatabaseService.execute_query(query)


def search_assessment_by_patient_id(patient_id):

    query = (
        supabase
        .table("pain_assessments")
        .select("*")
        .eq("patient_id", patient_id)
    )

    return DatabaseService.execute_query(query)


def search_assessment_by_pain_area(pain_area):

    query = (
        supabase
        .table("pain_assessments")
        .select("*")
        .ilike(
            "pain_areas",
            f"%{pain_area}%"
        )
    )

    return DatabaseService.execute_query(query)