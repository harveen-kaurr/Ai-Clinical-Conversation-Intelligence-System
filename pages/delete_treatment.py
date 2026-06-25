import streamlit as st
from services.treatment_crud import (
    get_treatment_by_id,
    delete_treatment
)

def show_delete_treatment_page():
    st.markdown('<h2 class="gradient-header" style="color: #dc2626;">Delete Treatment Session</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Permanently remove a logged treatment session record from the database.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    load_col1, load_col2 = st.columns([3, 1])
    with load_col1:
        treatment_id = st.text_input(
            "Enter Treatment UUID",
            placeholder="e.g. 12345678-1234-1234-1234-123456789012"
        )
    with load_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        load_btn = st.button("Load Treatment")
    st.markdown('</div>', unsafe_allow_html=True)

    if load_btn:
        if not treatment_id.strip():
            st.error("Please enter a valid Treatment UUID.")
            return

        with st.spinner("Retrieving treatment details..."):
            treatment = get_treatment_by_id(treatment_id.strip())

        if treatment:
            st.session_state["delete_treatment"] = treatment
            st.session_state["delete_treatment_id"] = treatment_id.strip()
            st.success("Treatment session loaded successfully!")
        else:
            st.error("Treatment session not found. Please verify the UUID.")

    if "delete_treatment" in st.session_state:
        treatment = st.session_state["delete_treatment"]
        del_id = st.session_state["delete_treatment_id"]

        st.markdown('<div class="custom-card" style="border-left: 5px solid #dc2626;">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#dc2626; margin-top:0;'>⚠️ Confirm Treatment Session Deletion</h4>", unsafe_allow_html=True)
        
        status = treatment.get('treatment_status', 'N/A')
        st.markdown(f"""
        <div style="margin-bottom: 20px; font-size: 0.95rem; line-height: 1.6;">
            <strong>Therapy Type:</strong> {treatment.get('treatment_type')}<br/>
            <strong>Session Date:</strong> {treatment.get('session_date')}<br/>
            <strong>Session Number:</strong> {treatment.get('session_number')}<br/>
            <strong>Treatment Status:</strong> {status}<br/>
            <strong>Consultation ID:</strong> <code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.8rem;">{treatment.get('consultation_id')}</code><br/>
            <strong>Treatment UUID:</strong> <code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.8rem;">{del_id}</code>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background: #fafafa; border-radius: 6px; padding: 12px; margin-bottom: 20px; font-size: 0.85rem; color: #475569; border: 1px dashed #e2e8f0;">
            <strong>Treatment Plan details:</strong> {treatment.get('treatment_plan') or 'N/A'}<br/>
            <strong>Remarks / Notes:</strong> {treatment.get('notes') or 'N/A'}
        </div>
        """, unsafe_allow_html=True)

        st.error("🚨 WARNING: This action is irreversible. The selected treatment session record will be permanently deleted from the database.")

        confirm = st.checkbox("I understand and confirm I want to delete this treatment record.")
        
        if confirm:
            if st.button("Delete Treatment"):
                with st.spinner("Deleting treatment session from database..."):
                    try:
                        result = delete_treatment(del_id)
                        if result:
                            st.success("Treatment session deleted successfully.")
                            del st.session_state["delete_treatment"]
                            del st.session_state["delete_treatment_id"]
                        else:
                            st.error("Delete operation failed. Please check database permissions.")
                    except Exception as exc:
                        st.error(f"Error deleting treatment: {exc}")
        st.markdown('</div>', unsafe_allow_html=True)
