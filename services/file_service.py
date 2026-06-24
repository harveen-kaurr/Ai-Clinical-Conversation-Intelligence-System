import uuid

from database.supabase_client import supabase
from database.database_service import DatabaseService


BUCKET_NAME = "consultation-reports"


class FileService:

    @staticmethod
    def upload_file(
        consultation_id: str,
        uploaded_file,
        file_type: str
    ):

        file_extension = (
            uploaded_file.name.split(".")[-1]
        )

        file_path = (
            f"{consultation_id}/"
            f"{uuid.uuid4()}.{file_extension}"
        )

        file_bytes = (
            uploaded_file.getvalue()
        )

        supabase.storage.from_(
            BUCKET_NAME
        ).upload(
            file_path,
            file_bytes
        )

        file_url = (
            supabase.storage
            .from_(BUCKET_NAME)
            .get_public_url(file_path)
        )

        metadata = {
            "consultation_id":
                consultation_id,

            "file_name":
                uploaded_file.name,

            "file_type":
                file_type,

            "file_url":
                file_url
        }

        query = (
            supabase
            .table("consultation_reports")
            .insert(metadata)
        )

        DatabaseService.execute_query(
            query
        )

        return metadata