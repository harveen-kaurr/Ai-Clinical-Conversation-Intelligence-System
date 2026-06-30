import streamlit as st

from services.ai_crud import (
    get_all_analysis
)


def show_view_ai_analysis_page():

    st.markdown(
        '<h2 class="gradient-header">AI Clinical Analysis</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom:20px;">'
        'View AI-generated clinical insights for all conversations.'
        '</p>',
        unsafe_allow_html=True
    )

    analyses = get_all_analysis()

    if not analyses:

        st.warning(
            "No AI analyses found."
        )

        return

    for analysis in analyses:

        with st.expander(

            f"Conversation ID: {analysis['conversation_id']}"

        ):

            st.subheader(
                "Clinical Summary"
            )

            st.write(
                analysis.get(
                    "summary",
                    "N/A"
                )
            )

            st.subheader(
                "Extracted Symptoms"
            )

            st.write(
                analysis.get(
                    "extracted_symptoms",
                    "N/A"
                )
            )

            st.subheader(
                "Pain Keywords"
            )

            st.write(
                analysis.get(
                    "pain_keywords",
                    "N/A"
                )
            )

            st.subheader(
                "Emotional State"
            )

            st.write(
                analysis.get(
                    "emotional_state",
                    "N/A"
                )
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Risk Level",
                    analysis.get(
                        "risk_level",
                        "N/A"
                    )
                )

                st.metric(
                    "Surgery Probability",
                    f"{analysis.get('surgery_probability',0)}%"
                )

            with col2:

                st.metric(
                    "Recovery Prediction",
                    analysis.get(
                        "recovery_prediction",
                        "N/A"
                    )
                )

                st.metric(
                    "AI Confidence",
                    f"{analysis.get('ai_confidence',0)}%"
                )

            st.subheader(
                "Recommendations"
            )

            st.write(
                analysis.get(
                    "recommendations",
                    "N/A"
                )
            )

            st.subheader(
                "Structured Output"
            )

            st.json(
                analysis.get(
                    "structured_output",
                    {}
                )
            )