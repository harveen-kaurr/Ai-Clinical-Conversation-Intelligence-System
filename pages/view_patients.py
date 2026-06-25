import streamlit as st
import pandas as pd

from services.patient_crud import get_all_patients


def show_view_patients_page():

    st.markdown('<h2 class="gradient-header">View Patients</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">List of all patient records currently stored in the system. Use the dashboard below to get quick analytics.</p>', unsafe_allow_html=True)

    with st.spinner("Loading patients from database..."):
        patients = get_all_patients()

    if not patients:
        st.warning("No patients found in the database. Please add a patient first.")
        return

    df = pd.DataFrame(patients)

    # Compute key stats
    total_patients = len(df)
    avg_age = round(df['age'].mean(), 1) if 'age' in df.columns else 0
    
    male_count = len(df[df['gender'].astype(str).str.lower() == 'male']) if 'gender' in df.columns else 0
    female_count = len(df[df['gender'].astype(str).str.lower() == 'female']) if 'gender' in df.columns else 0
    
    avg_bmi = round(df['bmi'].mean(), 2) if 'bmi' in df.columns and not df['bmi'].isnull().all() else "N/A"

    # Display Metrics Header inside a card
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Total Patients", f"{total_patients}")
    with m2:
        st.metric("Average Age", f"{avg_age} yrs")
    with m3:
        st.metric("Gender (M / F / O)", f"{male_count} / {female_count} / {total_patients - male_count - female_count}")
    with m4:
        st.metric("Average BMI", f"{avg_bmi}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Display main data table
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:0; color:#1e3a8a;">📋 Patient Master Records</h4>', unsafe_allow_html=True)
    st.dataframe(
        df,
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)