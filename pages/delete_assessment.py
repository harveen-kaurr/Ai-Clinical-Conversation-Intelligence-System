import streamlit as st
import pandas as pd

from services.pain_assessment_crud import (
    get_assessment_by_id,
    delete_assessment
)


def show_delete_assessment_page():

    st.markdown('<h2 class="gradient-header" style="color: #dc2626;">Delete Pain Assessment</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Permanently erase an assessment log from the database.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    load_col1, load_col2 = st.columns([3, 1])
    with load_col1:
        assessment_id = st.text_input(
            "Enter Assessment ID (UUID)"
        )
    with load_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        load_btn = st.button("Load Assessment")
    st.markdown('</div>', unsafe_allow_html=True)

    if load_btn:
        with st.spinner("Loading assessment log..."):
            assessment = get_assessment_by_id(
                assessment_id
            )

        if assessment:
            st.session_state["delete_assessment"] = assessment[0]
            st.session_state["delete_assessment_id"] = assessment_id
        else:
            st.error("Assessment not found. Please verify the UUID.")

    if "delete_assessment" in st.session_state:
        assessment = st.session_state["delete_assessment"]

        st.markdown('<div class="custom-card" style="border-left: 5px solid #dc2626;">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#dc2626; margin-top:0;'>⚠️ Confirm Assessment Deletion</h4>", unsafe_allow_html=True)

        st.markdown(f"""
        <div style="margin-bottom: 20px; font-size: 0.95rem; line-height: 1.6;">
            <strong>Patient ID:</strong> <code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.8rem;">{assessment.get('patient_id')}</code><br/>
            <strong>Pain Areas:</strong> {assessment.get('pain_areas')}<br/>
            <strong>Pain Severity:</strong> {assessment.get('pain_severity')} / 10<br/>
            <strong>Posture Observation:</strong> {assessment.get('posture')}<br/>
            <strong>Notes:</strong> {assessment.get('notes') or 'N/A'}
        </div>
        """, unsafe_allow_html=True)

        st.error("🚨 WARNING: This action cannot be undone. This pain assessment log will be permanently lost.")

        confirm = st.checkbox("I confirm I want to permanently delete this assessment.")
        if confirm:
            if st.button("Delete Assessment"):
                with st.spinner("Deleting assessment log..."):
                    result = delete_assessment(
                        st.session_state["delete_assessment_id"]
                    )

                if result:
                    st.success("Assessment log deleted successfully!")
                    del st.session_state["delete_assessment"]
                    del st.session_state["delete_assessment_id"]
                else:
                    st.error("Delete operation failed. Please check permissions.")
        st.markdown('</div>', unsafe_allow_html=True)