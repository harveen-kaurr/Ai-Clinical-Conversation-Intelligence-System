import streamlit as st
import pandas as pd

from services.pain_assessment_crud import (
    get_all_assessments
)


def show_view_assessment_page():

    st.markdown('<h2 class="gradient-header">View Assessments</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Review physical diagnosis profiles, pain metrics, and posture observations registered in the system.</p>', unsafe_allow_html=True)

    with st.spinner("Loading assessments..."):
        assessments = get_all_assessments()

    if not assessments:
        st.info("No assessments found in the database. Please add one first.")
        return

    df = pd.DataFrame(assessments)

    # Compute key stats
    total_assessments = len(df)
    avg_severity = round(df['pain_severity'].mean(), 1) if 'pain_severity' in df.columns else 0
    common_posture = df['posture'].mode().iloc[0] if 'posture' in df.columns and not df['posture'].empty else "N/A"

    # Display Metrics Header inside a card
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total Assessments", f"{total_assessments}")
    with m2:
        st.metric("Average Pain Severity", f"{avg_severity} / 10")
    with m3:
        st.metric("Common Posture Anomaly", f"{common_posture}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Display data table in a card container
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:0; color:#1e3a8a;">📋 Physical Assessments List</h4>', unsafe_allow_html=True)
    st.dataframe(
        df,
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)