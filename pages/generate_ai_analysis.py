import streamlit as st

from services.conversation_crud import (
    get_all_conversations
)

from services.ai_service import (
    AIService
)

from services.ai_crud import (
    create_analysis
)


def show_generate_ai_analysis_page():

    st.markdown(
        '<h2 class="gradient-header">Generate AI Clinical Analysis</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom:20px;">'
        'Generate AI-powered clinical insights from recorded doctor-patient conversations.'
        '</p>',
        unsafe_allow_html=True
    )

    conversations = get_all_conversations()

    if not conversations:

        st.warning(
            "No conversations available."
        )

        return

    conversation_map = {

        item["conversation_id"]: item

        for item in conversations

    }

    selected = st.selectbox(

        "Select Conversation",

        list(
            conversation_map.keys()
        )

    )

    conversation = conversation_map[selected]

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.info(

            f"**Source:** {conversation.get('source','N/A')}"

        )

        st.info(

            f"**Language:** {conversation.get('language','N/A')}"

        )

    with col2:

        st.info(

            f"**Emotion:** {conversation.get('emotional_state','N/A')}"

        )

        audio_url = conversation.get(
            "audio_file_url"
        )

        if audio_url:

            st.link_button(

                "Open Recorded Audio",

                audio_url,

                use_container_width=True

            )

    st.divider()

    transcript = st.text_area(

        "Whisper Transcript",

        value=conversation.get(

            "raw_transcript",

            ""

        ),

        height=300,

        help="Transcript generated automatically using Whisper AI. You may edit it before AI analysis."

    )

    if st.button(

        "Generate AI Analysis",

        use_container_width=True,

        type="primary"

    ):

        with st.spinner(

            "Running Gemini AI and Clinical Decision Engine..."

        ):

            try:

                payload = (

                    AIService.analyze_conversation(

                        {

                            "conversation_id":

                            conversation["conversation_id"],

                            "transcript":

                            transcript

                        }

                    )

                )

                create_analysis(
                    payload
                )

                st.success(

                    "AI Analysis Generated Successfully."

                )

                st.balloons()

                st.divider()

                st.subheader(
                    "Clinical Summary"
                )

                st.write(
                    payload["summary"]
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.metric(

                        "Risk",

                        payload["risk_level"]

                    )

                with col2:

                    st.metric(

                        "Surgery",

                        payload["surgery_probability"]

                    )

                with col3:

                    st.metric(

                        "Recovery",

                        payload["recovery_prediction"]

                    )

                with col4:

                    st.metric(

                        "Confidence",

                        payload["ai_confidence"]

                    )

                st.divider()

                st.subheader(
                    "Symptoms"
                )

                st.write(
                    payload["extracted_symptoms"]
                )

                st.subheader(
                    "Pain Keywords"
                )

                st.write(
                    payload["pain_keywords"]
                )

                st.subheader(
                    "Recommendations"
                )

                st.success(
                    payload["recommendations"]
                )

                structured = payload.get(
                    "structured_output",
                    {}
                )

                rules = structured.get(
                    "clinical_rules",
                    {}
                )

                prediction = structured.get(
                    "prediction_engine",
                    {}
                )

                st.divider()

                st.subheader(
                    "Clinical Rules"
                )

                c1, c2 = st.columns(2)

                with c1:

                    st.write(

                        f"**Follow-up:** {rules.get('follow_up','N/A')}"

                    )

                    st.write(

                        f"**Rule Risk:** {rules.get('rule_risk_level','N/A')}"

                    )

                    st.write(

                        f"**Rule Surgery Probability:** {rules.get('rule_surgery_probability','N/A')}"

                    )

                with c2:

                    st.write("**Suggested Tests**")

                    for test in rules.get(

                        "suggested_tests",

                        []

                    ):

                        st.success(test)

                st.subheader(

                    "Recommended Therapy"

                )

                therapy = rules.get(

                    "recommended_therapy",

                    []

                )

                if therapy:

                    cols = st.columns(2)

                    for i, item in enumerate(therapy):

                        with cols[i % 2]:

                            st.info(item)

                st.subheader(

                    "Prediction Engine"

                )

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(

                        "Pain Level",

                        prediction.get(
                            "pain_level",
                            "N/A"
                        )

                    )

                    st.metric(

                        "Patient Category",

                        prediction.get(
                            "patient_category",
                            "N/A"
                        )

                    )

                with c2:

                    st.metric(

                        "Therapy Priority",

                        prediction.get(
                            "therapy_priority",
                            "N/A"
                        )

                    )

                    st.metric(

                        "Recovery Priority",

                        prediction.get(
                            "recovery_priority",
                            "N/A"
                        )

                    )

            except Exception as e:

                st.error(
                    str(e)
                )