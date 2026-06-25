from services.conversation_service import (
    ConversationService
)


def print_result(title, success, message):

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    if success:
        print(f"✅ PASS : {message}")
    else:
        print(f"❌ FAIL : {message}")


def test_valid_conversation():

    try:

        conversation = {

            "consultation_id":
                "12345678-1234-1234-1234-123456789012",

            "source":
                "Manual",

            "raw_transcript":
                "Patient reports lower back pain.",

            "language":
                "English",

            "speaker_separation":
                "Doctor: Hello\nPatient: My back hurts.",

            "emotional_state":
                "Calm",

            "pain_keywords":
                "Lower Back Pain",

            "additional_notes":
                "Patient advised to rest."
        }

        ConversationService.register_conversation(
            conversation
        )

        print_result(
            "VALID CONVERSATION TEST",
            True,
            "Conversation validated successfully."
        )

    except Exception as e:

        print_result(
            "VALID CONVERSATION TEST",
            False,
            str(e)
        )


def test_missing_consultation_id():

    try:

        conversation = {

            "source":
                "Manual",

            "raw_transcript":
                "Sample transcript"
        }

        ConversationService.register_conversation(
            conversation
        )

        print_result(
            "MISSING CONSULTATION ID",
            False,
            "Validation should have failed."
        )

    except Exception as e:

        print_result(
            "MISSING CONSULTATION ID",
            True,
            str(e)
        )


def test_missing_source():

    try:

        conversation = {

            "consultation_id":
                "12345678-1234-1234-1234-123456789012",

            "raw_transcript":
                "Sample transcript"
        }

        ConversationService.register_conversation(
            conversation
        )

        print_result(
            "MISSING SOURCE",
            False,
            "Validation should have failed."
        )

    except Exception as e:

        print_result(
            "MISSING SOURCE",
            True,
            str(e)
        )


def test_missing_transcript():

    try:

        conversation = {

            "consultation_id":
                "12345678-1234-1234-1234-123456789012",

            "source":
                "Manual"
        }

        ConversationService.register_conversation(
            conversation
        )

        print_result(
            "MISSING TRANSCRIPT",
            True,
            "Validation should have failed."
        )

    except Exception as e:

        print_result(
            "MISSING TRANSCRIPT",
            True,
            str(e)
        )


if __name__ == "__main__":

    print("\n")
    print("=" * 50)
    print("CONVERSATION SERVICE TEST REPORT")
    print("=" * 50)

    test_valid_conversation()

    test_missing_consultation_id()

    test_missing_source()

    test_missing_transcript()

    print("\n")
    print("=" * 50)
    print("ALL TESTS COMPLETED")
    print("=" * 50)