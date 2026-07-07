from models.conversation import (
    ConversationCreate
)


class ConversationService:

    REQUIRED_FIELDS = [
        "consultation_id",
        "source"
    ]

    @staticmethod
    def validate_conversation(
        conversation_data: dict
    ) -> None:

        # Validate common required fields
        for field in ConversationService.REQUIRED_FIELDS:

            if (
                field not in conversation_data
                or conversation_data[field] is None
                or conversation_data[field] == ""
            ):

                raise ValueError(
                    f"{field} is required"
                )

        # Require audio only when source is Audio Upload
        if (
            conversation_data.get("source") == "Audio Upload"
            and (
                "audio_file_url" not in conversation_data
                or conversation_data["audio_file_url"] is None
                or conversation_data["audio_file_url"] == ""
            )
        ):
            raise ValueError(
                "audio_file_url is required"
            )

    @staticmethod
    def create_conversation_payload(
        conversation_data: dict
    ) -> dict:

        payload = conversation_data.copy()

        return payload

    @staticmethod
    def register_conversation(
        conversation_data: dict
    ) -> dict:

        ConversationService.validate_conversation(
            conversation_data
        )

        payload = (
            ConversationService.create_conversation_payload(
                conversation_data
            )
        )

        ConversationCreate(**payload)

        return payload