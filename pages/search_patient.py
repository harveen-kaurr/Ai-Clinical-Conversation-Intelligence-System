import streamlit as st
import pandas as pd

from services.patient_crud import (
    search_patient_by_name,
    search_patient_by_phone,
    search_patient_by_patient_id
)


def show_search_patient_page():

    st.markdown('<h2 class="gradient-header">Search Patient Records</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Lookup patient accounts in the database by Name, Phone Number, or Unique UUID.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    search_col1, search_col2 = st.columns([1, 2])
    with search_col1:
        search_type = st.selectbox(
            "Search Parameter",
            [
                "Patient Name",
                "Phone Number",
                "Patient ID"
            ]
        )
    with search_col2:
        search_value = st.text_input(
            "Enter Search Term",
            placeholder=f"Enter {search_type.lower()}..."
        )
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Search Database"):

        if not search_value.strip():
            st.warning("Please enter a search query.")
            return

        with st.spinner("Searching records..."):
            if search_type == "Patient Name":
                results = search_patient_by_name(search_value)
            elif search_type == "Phone Number":
                results = search_patient_by_phone(search_value)
            else:
                results = search_patient_by_patient_id(search_value)

        if not results:
            st.error("No matching patient record found in the database.")
            return

        st.success(f"Found {len(results)} matching patient account(s).")

        # Render profile cards instead of a raw dataframe
        for patient in results:
            st.markdown(f"""
            <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
                <div style="border-bottom: 1px solid #f1f5f9; padding-bottom: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; color: #1e3a8a; font-weight: 700; font-size:1.25rem;">👤 {patient.get('patient_name')}</h3>
                    <span style="background: #e0f2fe; color: #0369a1; font-size: 0.75rem; font-weight: 700; padding: 4px 8px; border-radius: 100px;">Patient Account</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; font-size: 0.9rem;">
                    <div><span style="color:#64748b; font-weight:500;">Patient ID:</span><br/><code style="background:#f1f5f9; color:#0f172a; padding: 2px 6px; border-radius:4px; font-size:0.8rem;">{patient.get('patient_id')}</code></div>
                    <div><span style="color:#64748b; font-weight:500;">Age / Gender:</span><br/>{patient.get('age')} years / {patient.get('gender')}</div>
                    <div><span style="color:#64748b; font-weight:500;">Contact Phone:</span><br/>{patient.get('phone_number')}</div>
                    <div><span style="color:#64748b; font-weight:500;">Email Address:</span><br/>{patient.get('email') or 'N/A'}</div>
                    <div><span style="color:#64748b; font-weight:500;">Primary Complaint:</span><br/><span style="color:#0d9488; font-weight:600;">{patient.get('disease') or 'N/A'}</span></div>
                    <div><span style="color:#64748b; font-weight:500;">Date of Visiting:</span><br/>{patient.get('date_of_visiting') or 'N/A'}</div>
                    <div><span style="color:#64748b; font-weight:500;">BMI Status:</span><br/>{patient.get('bmi') or 'N/A'} ({patient.get('bmi_category') or 'N/A'})</div>
                    <div><span style="color:#64748b; font-weight:500;">Emergency Contact:</span><br/>{patient.get('emergency_contact') or 'N/A'}</div>
                </div>
                {f'<div style="margin-top: 15px; padding-top: 10px; border-top: 1px dashed #f1f5f9; font-size:0.85rem; color:#475569;"><strong>Spine Injury History:</strong> {patient.get("previous_spine_injury")}</div>' if patient.get("previous_spine_injury") else ''}
            </div>
            """, unsafe_allow_html=True)