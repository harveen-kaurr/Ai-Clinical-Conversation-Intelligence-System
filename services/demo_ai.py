from services.ai_service import AIService

from services.ai_crud import create_analysis


def main():

    analysis_data = {

        "conversation_id":
            input(
                "Enter Conversation ID: "
            ),

        "transcript":
            input(
                "Enter Transcript: "
            )

    }

    try:

        payload = (
            AIService.analyze_conversation(
                analysis_data
            )
        )

        create_analysis(
            payload
        )

        print("\nAI Analysis Saved Successfully\n")

        print(payload)

    except Exception as e:

        print(
            f"\nError: {e}"
        )


if __name__ == "__main__":

    main()