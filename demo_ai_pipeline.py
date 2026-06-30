from services.ai_service import AIService
from services.ai_crud import create_analysis


def main():

    conversation_id = input(
        "Conversation ID: "
    )

    transcript = input(
        "Transcript: "
    )

    analysis_data = {

        "conversation_id":
            conversation_id,

        "transcript":
            transcript

    }

    payload = (
        AIService.analyze_conversation(
            analysis_data
        )
    )

    create_analysis(
        payload
    )

    print("\n========== AI PIPELINE ==========\n")

    print(
        f"Risk Level : {payload['risk_level']}"
    )

    print(
        f"Surgery Probability : {payload['surgery_probability']}"
    )

    print(
        f"Recovery Prediction : {payload['recovery_prediction']}"
    )

    print(
        f"Confidence : {payload['ai_confidence']}"
    )

    print("\nRecommendations:\n")

    print(
        payload["recommendations"]
    )

    print("\nStructured Output:\n")

    print(
        payload["structured_output"]
    )


if __name__ == "__main__":

    main()