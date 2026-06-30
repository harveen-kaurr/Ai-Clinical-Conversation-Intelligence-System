import streamlit as st
import pandas as pd
import json

from services.ai_crud import (
    get_all_analysis
)


def show_ai_dashboard_page():

    st.markdown(
        '<h2 class="gradient-header">AI Clinical Analytics Dashboard</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#64748b;margin-top:-10px;">'
        'Overview of AI-generated clinical insights and patient risk analytics.'
        '</p>',
        unsafe_allow_html=True
    )

    analyses = get_all_analysis()

    if not analyses:

        st.warning(
            "No AI analyses available."
        )

        return

    df = pd.DataFrame(analyses)

    total_reports = len(df)

    high_risk = len(

        df[
            df["risk_level"]
            .astype(str)
            .str.contains(
                "high",
                case=False,
                na=False
            )
        ]

    )

    avg_confidence = round(

        pd.to_numeric(

            df["ai_confidence"],

            errors="coerce"

        ).fillna(0).mean(),

        2

    )

    avg_surgery = round(

        pd.to_numeric(

            df["surgery_probability"],

            errors="coerce"

        ).fillna(0).mean(),

        2

    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "AI Reports",
        total_reports
    )

    col2.metric(
        "High Risk",
        high_risk
    )

    col3.metric(
        "Avg Confidence",
        f"{avg_confidence}%"
    )

    col4.metric(
        "Avg Surgery %",
        f"{avg_surgery}%"
    )

    st.divider()

    pain_levels = []

    patient_categories = []

    therapy_priorities = []

    recovery_priorities = []

    emotions = []

    for row in analyses:

        emotions.append(

            row.get(

                "emotional_state",

                "Unknown"

            )

        )

        structured = row.get(

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

        prediction = structured.get(

            "prediction_engine",

            {}

        )

        pain_levels.append(

            prediction.get(

                "pain_level",

                "Unknown"

            )

        )

        patient_categories.append(

            prediction.get(

                "patient_category",

                "Unknown"

            )

        )

        therapy_priorities.append(

            prediction.get(

                "therapy_priority",

                "Unknown"

            )

        )

        recovery_priorities.append(

            prediction.get(

                "recovery_priority",

                "Unknown"

            )

        )

    c1, c2 = st.columns(2)

    with c1:

        st.subheader(
            "Risk Distribution"
        )

        st.bar_chart(

            df["risk_level"]

            .value_counts()

        )

    with c2:

        st.subheader(
            "Emotion Distribution"
        )

        st.bar_chart(

            pd.Series(

                emotions

            ).value_counts()

        )

    c1, c2 = st.columns(2)

    with c1:

        st.subheader(
            "Pain Level"
        )

        st.bar_chart(

            pd.Series(

                pain_levels

            ).value_counts()

        )

    with c2:

        st.subheader(
            "Patient Category"
        )

        st.bar_chart(

            pd.Series(

                patient_categories

            ).value_counts()

        )

    c1, c2 = st.columns(2)

    with c1:

        st.subheader(
            "Therapy Priority"
        )

        st.bar_chart(

            pd.Series(

                therapy_priorities

            ).value_counts()

        )

    with c2:

        st.subheader(
            "Recovery Priority"
        )

        st.bar_chart(

            pd.Series(

                recovery_priorities

            ).value_counts()

        )

    st.divider()

    st.subheader(
        "AI Confidence"
    )

    st.line_chart(

        pd.to_numeric(

            df["ai_confidence"],

            errors="coerce"

        )

    )

    st.subheader(
        "Surgery Probability"
    )

    st.line_chart(

        pd.to_numeric(

            df["surgery_probability"],

            errors="coerce"

        )

    )

    st.divider()

    st.subheader(
        "Recent AI Reports"
    )

    columns = [

        "conversation_id",

        "risk_level",

        "surgery_probability",

        "ai_confidence"

    ]

    st.dataframe(

        df[columns],

        use_container_width=True,

        hide_index=True

    )