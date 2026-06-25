import streamlit as st
import pandas as pd

from services.consultation_crud import (
    search_consultations
)


def show_search_consultation_page():

    st.markdown('<h2 class="gradient-header">Search Consultations</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Find historical clinical encounters by Patient ID or Doctor Name.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>🔍 Search Parameters</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        patient_id = st.text_input(
            "Filter by Patient ID (UUID)",
            placeholder="e.g. bb544e9c-7013-4a6f-82ce-8ad5b15e4573"
        )
    with col2:
        doctor_name = st.text_input(
            "Filter by Doctor Name",
            placeholder="e.g. Dr. Rajat"
        )
    st.markdown('</div>', unsafe_allow_html=True)

    search = st.button(
        "Search Clinical Logs"
    )

    if search:
        if not patient_id.strip() and not doctor_name.strip():
            st.warning("Please enter at least one search filter (Patient ID or Doctor Name).")
            return

        with st.spinner("Searching consultations..."):
            consultations = search_consultations(
                patient_id=patient_id.strip() if patient_id.strip() else None,
                doctor_name=doctor_name.strip() if doctor_name.strip() else None
            )

        if not consultations:
            st.error("No consultation records found matching these criteria.")
            return

        st.success(f"Found {len(consultations)} matching clinical encounter(s).")

        for idx, enc in enumerate(consultations):
            st.markdown(f"""
            <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
                <div style="border-bottom: 1px solid #f1f5f9; padding-bottom: 12px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h3 style="margin: 0; color: #1e3a8a; font-weight: 700; font-size:1.15rem;">👨‍⚕️ {enc.get('doctor_name')}</h3>
                        <p style="margin: 2px 0 0 0; font-size: 0.8rem; color:#64748b;">Specialization: {enc.get('specialization')}</p>
                    </div>
                    <div style="text-align: right;">
                        <span style="background: #f0fdf4; color: #166534; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 100px; border: 1px solid #bbf7d0;">Encounter Logged</span>
                        <p style="margin: 4px 0 0 0; font-size: 0.75rem; color:#94a3b8;">{enc.get('consultation_date')} at {enc.get('consultation_time')}</p>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; font-size: 0.9rem; margin-bottom: 15px;">
                    <div><span style="color:#64748b; font-weight:500;">Patient ID:</span><br/><code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.75rem;">{enc.get('patient_id')}</code></div>
                    <div><span style="color:#64748b; font-weight:500;">Consultation ID:</span><br/><code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.75rem;">{enc.get('consultation_id')}</code></div>
                    <div><span style="color:#64748b; font-weight:500;">Recommended Imaging:</span><br/><strong>{enc.get('recommended_scan') or 'None'}</strong></div>
                    <div><span style="color:#64748b; font-weight:500;">Follow-up Date:</span><br/>{enc.get('followup_date') or 'No follow-up set'}</div>
                </div>

                <div style="background: #f8fafc; border-radius: 6px; padding: 12px; margin-bottom: 15px; font-size: 0.9rem; border-left: 3px solid #3b82f6;">
                    <strong>Chief Complaint:</strong><br/>
                    {enc.get('chief_complaint')}
                </div>

                <div style="background: #f8fafc; border-radius: 6px; padding: 12px; margin-bottom: 15px; font-size: 0.9rem; border-left: 3px solid #0d9488;">
                    <strong>Clinical Findings Summary:</strong><br/>
                    {enc.get('clinical_findings') or 'No findings logged.'}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Nested expander for detailed examinations to avoid page clutter
            with st.expander("🔍 View Detailed Physical Examinations Notes"):
                st.markdown(f"""
                <div style="font-size:0.85rem; line-height: 1.6;">
                    <p><strong>Spine Examination:</strong> {enc.get('spine_exam') or 'N/A'}</p>
                    <p><strong>Muscle Examination:</strong> {enc.get('muscle_exam') or 'N/A'}</p>
                    <p><strong>Nerve Examination:</strong> {enc.get('nerve_exam') or 'N/A'}</p>
                    <p><strong>Tissue Examination:</strong> {enc.get('tissue_exam') or 'N/A'}</p>
                    <p><strong>Bone & Joint Examination:</strong> {enc.get('bone_joint_exam') or 'N/A'}</p>
                    <p><strong>Preliminary Diagnosis:</strong> {enc.get('preliminary_diagnosis') or 'N/A'}</p>
                </div>
                """, unsafe_allow_html=True)