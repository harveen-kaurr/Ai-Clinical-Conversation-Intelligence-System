import streamlit as st
import pandas as pd

from services.consultation_crud import (
    get_all_consultations
)


def show_view_consultation_page():

    st.markdown('<h2 class="gradient-header">View Consultations</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Review all doctor visits, diagnostic tests recommendations, and follow-up schedules.</p>', unsafe_allow_html=True)

    with st.spinner("Loading consultations..."):
        consultations = get_all_consultations()

    if not consultations:
        st.info("No consultation logs found in the database. Please add one first.")
        return

    df = pd.DataFrame(consultations)

    # Compute key stats
    total_consultations = len(df)
    unique_doctors = df['doctor_name'].nunique() if 'doctor_name' in df.columns else 0
    scans_ordered = df['recommended_scan'].notnull().sum() if 'recommended_scan' in df.columns else 0

    # Display Metrics Header inside a card
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total Consultations", f"{total_consultations}")
    with m2:
        st.metric("Active Clinicians", f"{unique_doctors}")
    with m3:
        st.metric("Imaging Scans Ordered", f"{scans_ordered}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Display data table in a card container
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:0; color:#1e3a8a;">📋 Clinical Consultation Log</h4>', unsafe_allow_html=True)
    st.dataframe(
        df,
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)