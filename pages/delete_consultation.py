import streamlit as st
from services.consultation_crud import (
    get_consultation_by_id,
    delete_consultation
)

def show_delete_consultation_page():
    st.markdown('<h2 class="gradient-header" style="color: #dc2626;">Delete Clinical Consultation</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Permanently remove a clinical consultation record and any uploaded reports from the database.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    load_col1, load_col2 = st.columns([3, 1])
    with load_col1:
        consultation_id = st.text_input(
            "Enter Consultation UUID",
            placeholder="e.g. 12345678-1234-1234-1234-123456789012"
        )
    with load_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        load_btn = st.button("Load Consultation")
    st.markdown('</div>', unsafe_allow_html=True)

    if load_btn:
        if not consultation_id.strip():
            st.error("Please enter a valid Consultation UUID.")
            return

        with st.spinner("Retrieving consultation details..."):
            consultation = get_consultation_by_id(consultation_id.strip())

        if consultation:
            st.session_state["delete_consultation"] = consultation
            st.session_state["delete_consultation_id"] = consultation_id.strip()
            st.success("Consultation loaded successfully!")
        else:
            st.error("Consultation record not found. Please verify the UUID.")

    if "delete_consultation" in st.session_state:
        consultation = st.session_state["delete_consultation"]
        del_id = st.session_state["delete_consultation_id"]

        st.markdown('<div class="custom-card" style="border-left: 5px solid #dc2626;">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#dc2626; margin-top:0;'>⚠️ Confirm Consultation Deletion</h4>", unsafe_allow_html=True)

        st.markdown(f"""
        <div style="margin-bottom: 20px; font-size: 0.95rem; line-height: 1.6;">
            <strong>Doctor Name:</strong> {consultation.get('doctor_name')}<br/>
            <strong>Specialization:</strong> {consultation.get('specialization')}<br/>
            <strong>Date / Time:</strong> {consultation.get('consultation_date')} at {consultation.get('consultation_time')}<br/>
            <strong>Patient ID:</strong> <code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.8rem;">{consultation.get('patient_id')}</code><br/>
            <strong>Consultation UUID:</strong> <code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.8rem;">{del_id}</code>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background: #fafafa; border-radius: 6px; padding: 12px; margin-bottom: 20px; font-size: 0.85rem; color: #475569; border: 1px dashed #e2e8f0;">
            <strong>Chief Complaint:</strong> {consultation.get('chief_complaint') or 'N/A'}<br/>
            <strong>Preliminary Diagnosis:</strong> {consultation.get('preliminary_diagnosis') or 'N/A'}
        </div>
        """, unsafe_allow_html=True)

        st.error("🚨 WARNING: This action is irreversible. The selected clinical consultation record will be permanently deleted from the database.")

        confirm = st.checkbox("I understand and confirm I want to delete this consultation record.")

        if confirm:
            if st.button("Delete Consultation"):
                with st.spinner("Deleting clinical consultation from database..."):
                    try:
                        result = delete_consultation(del_id)
                        if result:
                            st.success("Clinical consultation record deleted successfully.")
                            # Clean session state keys
                            del st.session_state["delete_consultation"]
                            del st.session_state["delete_consultation_id"]
                        else:
                            st.error("Delete operation failed. Please check database permissions.")
                    except Exception as exc:
                        st.error(f"Error deleting consultation: {exc}")
        st.markdown('</div>', unsafe_allow_html=True)
