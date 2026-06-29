from models.conversation import (
    ConversationCreate
)


class ConversationService:

    REQUIRED_FIELDS = [

        "consultation_id",

        "source",

        "audio_file_url"
    ]

    @staticmethod
    def validate_conversation(
        conversation_data: dict
    ) -> None:

        for field in ConversationService.REQUIRED_FIELDS:

            if (
                field not in conversation_data
                or conversation_data[field] is None
                or conversation_data[field] == ""
            ):

                raise ValueError(
                    f"{field} is required"
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