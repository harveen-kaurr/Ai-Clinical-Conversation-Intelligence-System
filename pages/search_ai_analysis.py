import streamlit as st
import json

from services.ai_crud import (
    get_all_analysis
)


def show_search_ai_analysis_page():

    st.markdown(
        '<h2 class="gradient-header">Search AI Analysis</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom:20px;">'
        'Search AI-generated clinical reports.'
        '</p>',
        unsafe_allow_html=True
    )

    analyses = get_all_analysis()

    if not analyses:

        st.warning(
            "No AI analyses found."
        )

        return

    search = st.text_input(
        "Search Conversation ID"
    )

    if search:

        analyses = [

            item

            for item in analyses

            if search.lower()

            in item["conversation_id"].lower()

        ]

    if not analyses:

        st.warning(
            "No matching analysis found."
        )

        return

    analysis = analyses[0]

    st.success(
        "Analysis Found"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"**Conversation ID:** {analysis.get('conversation_id','N/A')}"
        )

    with col2:

        st.info(
            f"**Risk Level:** {analysis.get('risk_level','N/A')}"
        )

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
            analysis.get(
                "surgery_probability",
                0
            )
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
            analysis.get(
                "ai_confidence",
                0
            )
        )

    st.subheader(
        "Recommendations"
    )

    st.info(
        analysis.get(
            "recommendations",
            "N/A"
        )
    )

    structured = analysis.get(
        "structured_output",
        {}
    )

    if isinstance(
        structured,
        str
    ):

        try:

            structured = json.loads(
                structured
            )

        except:

            structured = {}

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

        st.write(
            f"**Rule Recovery Prediction:** {rules.get('rule_recovery_prediction','N/A')}"
        )

    with c2:

        st.write(
            "**Suggested Tests**"
        )

        tests = rules.get(
            "suggested_tests",
            []
        )

        if tests:

            for item in tests:

                st.success(item)

        else:

            st.info(
                "No suggested tests."
            )

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

    else:

        st.info(
            "No therapy recommendations."
        )

    st.subheader(
        "Clinical Flags"
    )

    flags = rules.get(
        "flags",
        []
    )

    if flags:

        cols = st.columns(3)

        for i, item in enumerate(flags):

            with cols[i % 3]:

                st.warning(item)

    else:

        st.info(
            "No clinical flags."
        )

    st.divider()

    st.subheader(
        "Prediction Engine"
    )

    col1, col2 = st.columns(2)

    with col1:

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

    with col2:

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

    with st.expander(
        "View Complete AI JSON"
    ):

        st.json(
            structured
        )