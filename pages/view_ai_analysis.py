import streamlit as st
import pandas as pd

from services.ai_crud import get_all_analysis


def show_view_ai_analysis_page():

    st.markdown('<h2 class="gradient-header">AI Clinical Analysis</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom:20px;">'
        'All AI-generated clinical analyses stored in the system. Use the table to review analysis IDs for lookup.</p>',
        unsafe_allow_html=True
    )

    with st.spinner("Loading analyses from database..."):
        analyses = get_all_analysis()

    if not analyses:
        st.warning("No AI analyses found in the database.")
        return

    df = pd.DataFrame(analyses)

    total = len(df)
    avg_confidence = round(df["ai_confidence"].mean(), 2) if "ai_confidence" in df.columns and not df["ai_confidence"].isnull().all() else "N/A"

    risk_counts = df["risk_level"].value_counts() if "risk_level" in df.columns else pd.Series()
    high_risk = int(risk_counts.get("High", 0))
    medium_risk = int(risk_counts.get("Medium", 0))
    low_risk = int(risk_counts.get("Low", 0))

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Total Analyses", total)
    with m2:
        st.metric("Avg AI Confidence", avg_confidence)
    with m3:
        st.metric("High / Medium Risk", f"{high_risk} / {medium_risk}")
    with m4:
        st.metric("Low Risk", low_risk)
    st.markdown('</div>', unsafe_allow_html=True)

    display_cols = [
        col for col in [
            "analysis_id", "conversation_id", "risk_level",
            "surgery_probability", "recovery_prediction", "ai_confidence", "emotional_state"
        ] if col in df.columns
    ]

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:0; color:#1e3a8a;">AI Analysis Records</h4>', unsafe_allow_html=True)
    st.dataframe(df[display_cols], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
