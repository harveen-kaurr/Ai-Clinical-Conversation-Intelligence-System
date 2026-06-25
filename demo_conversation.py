from services.conversation_service import (
    ConversationService
)


conversation = {

    "consultation_id":
        "12345678-1234-1234-1234-123456789012",

    "source":
        "Manual",

    "raw_transcript":
        "Patient complains of severe neck pain for two weeks.",

    "language":
        "English",

    "speaker_separation":
        "Doctor: Where is the pain?\nPatient: Neck region.",

    "emotional_state":
        "Anxious",

    "pain_keywords":
        "Neck Pain",

    "additional_notes":
        "MRI recommended."
}


try:

    payload = (
        ConversationService.register_conversation(
            conversation
        )
    )

    print("\n" + "=" * 55)
    print("CONVERSATION SERVICE DEMO")
    print("=" * 55)

    print("\n✅ Conversation Registered Successfully!\n")

    for key, value in payload.items():

        print(f"{key:22}: {value}")

    print("\n" + "=" * 55)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("=" * 55)

except Exception as e:

    print("\n" + "=" * 55)
    print("CONVERSATION SERVICE DEMO")
    print("=" * 55)

    print(f"\n❌ Error: {e}")

    print("\n" + "=" * 55)