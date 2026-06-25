import streamlit as st

from services.patient_crud import (
    get_patient_by_id,
    delete_patient
)


def show_delete_patient_page():

    st.markdown('<h2 class="gradient-header" style="color: #dc2626;">Delete Patient Record</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Permanently remove a patient record and all related assessments/consultations from the system.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    load_col1, load_col2 = st.columns([3, 1])
    with load_col1:
        patient_id = st.text_input(
            "Enter Patient UUID"
        )
    with load_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        load_btn = st.button("Load Patient")
    st.markdown('</div>', unsafe_allow_html=True)

    if load_btn:
        with st.spinner("Retrieving patient details..."):
            patient = get_patient_by_id(
                patient_id
            )

        if not patient:
            st.error("Patient not found in the database. Please verify the UUID.")
            return

        st.session_state["delete_patient"] = patient[0]

    if "delete_patient" in st.session_state:
        patient = st.session_state["delete_patient"]

        st.markdown('<div class="custom-card" style="border-left: 5px solid #dc2626;">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#dc2626; margin-top:0;'>⚠️ Confirm Patient Deletion</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="margin-bottom: 20px; font-size: 0.95rem; line-height: 1.6;">
            <strong>Patient Name:</strong> {patient['patient_name']}<br/>
            <strong>Gender / Age:</strong> {patient['gender']} / {patient['age']} years<br/>
            <strong>Phone Number:</strong> {patient['phone_number']}<br/>
            <strong>Patient ID:</strong> <code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.8rem;">{patient['patient_id']}</code>
        </div>
        """, unsafe_allow_html=True)

        st.error("🚨 WARNING: This action is irreversible. All consultation records and pain assessments linked to this patient will be permanently deleted.")

        confirm = st.checkbox("I understand and confirm I want to delete this patient record.")
        
        if confirm:
            if st.button("Delete Patient"):
                with st.spinner("Deleting patient record from database..."):
                    result = delete_patient(
                        patient["patient_id"]
                    )

                if result:
                    st.success("Patient record deleted successfully.")
                    del st.session_state["delete_patient"]
                else:
                    st.error("Delete operation failed. Please check permissions.")
        st.markdown('</div>', unsafe_allow_html=True)