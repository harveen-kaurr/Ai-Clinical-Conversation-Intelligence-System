import streamlit as st
import pandas as pd

from services.pain_assessment_crud import (
    search_assessment_by_patient_id
)


def show_search_assessment_page():

    st.markdown('<h2 class="gradient-header">Search Assessments</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Lookup patient pain assessment logs by entering their unique Patient UUID.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    search_col1, search_col2 = st.columns([3, 1])
    with search_col1:
        patient_id = st.text_input(
            "Enter Patient ID (UUID)",
            placeholder="e.g. bb544e9c-7013-4a6f-82ce-8ad5b15e4573"
        )
    with search_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        search_btn = st.button("Search Logs")
    st.markdown('</div>', unsafe_allow_html=True)

    if search_btn:
        if not patient_id.strip():
            st.warning("Please enter a valid Patient UUID to search.")
            return

        with st.spinner("Searching assessment logs..."):
            assessments = search_assessment_by_patient_id(patient_id.strip())

        if not assessments:
            st.error("No assessment logs found for this Patient ID.")
            return

        st.success(f"Found {len(assessments)} pain assessment log(s) for this patient.")

        for idx, item in enumerate(assessments):
            # Define severity badge styling based on value
            severity = item.get('pain_severity', 0)
            if severity <= 3:
                badge_style = "background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0;"
                label = "Mild Pain"
            elif severity <= 7:
                badge_style = "background: #fef9c3; color: #a16207; border: 1px solid #fef08a;"
                label = "Moderate Pain"
            else:
                badge_style = "background: #fee2e2; color: #b91c1c; border: 1px solid #fecaca;"
                label = "Severe Pain"

            st.markdown(f"""
            <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
                <div style="border-bottom: 1px solid #f1f5f9; padding-bottom: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0; color: #1e3a8a; font-weight: 700;">📋 Assessment #{idx+1}</h4>
                    <span style="font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 100px; {badge_style}">{label} ({severity}/10)</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; font-size: 0.9rem; margin-bottom: 10px;">
                    <div><span style="color:#64748b; font-weight:500;">Observed Posture:</span><br/><strong>{item.get('posture')}</strong></div>
                    <div><span style="color:#64748b; font-weight:500;">Logged Pain Areas:</span><br/><span style="color:#0d9488; font-weight:600;">{item.get('pain_areas')}</span></div>
                    <div><span style="color:#64748b; font-weight:500;">Recorded Date:</span><br/>{item.get('created_at')}</div>
                    <div><span style="color:#64748b; font-weight:500;">Assessment UUID:</span><br/><code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.75rem;">{item.get('assessment_id')}</code></div>
                </div>
                <div style="margin-top: 10px; padding-top: 10px; border-top: 1px dashed #f1f5f9; font-size:0.85rem; color:#475569;">
                    <strong>Observation Notes:</strong> {item.get('notes') or 'No additional notes provided.'}
                </div>
            </div>
            """, unsafe_allow_html=True)