import uuid

from database.supabase_client import (
    supabase
)


ALLOWED_EXTENSIONS = [
    "mp3",
    "wav",
    "m4a"
]

MAX_FILE_SIZE = 50 * 1024 * 1024   # 50 MB

BUCKET_NAME = "conversation-audio"


class AudioService:

    @staticmethod
    def validate_audio(uploaded_file):

        file_extension = (
            uploaded_file.name
            .split(".")[-1]
            .lower()
        )

        if file_extension not in ALLOWED_EXTENSIONS:

            raise ValueError(
                f"Invalid file type. Allowed types: {ALLOWED_EXTENSIONS}"
            )

        file_size = len(
            uploaded_file.getvalue()
        )

        if file_size > MAX_FILE_SIZE:

            raise ValueError(
                "Audio file exceeds 50 MB limit."
            )

    @staticmethod
    def upload_audio(
        consultation_id: str,
        uploaded_file
    ):

        AudioService.validate_audio(
            uploaded_file
        )

        file_extension = (
            uploaded_file.name
            .split(".")[-1]
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

        audio_url = (
            supabase.storage
            .from_(BUCKET_NAME)
            .get_public_url(
                file_path
            )
        )

        return audio_url