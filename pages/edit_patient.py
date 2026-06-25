import streamlit as st

from services.patient_crud import (
    get_patient_by_id,
    update_patient
)


def show_edit_patient_page():

    st.markdown('<h2 class="gradient-header">Edit Patient Record</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Retrieve a patient by their unique ID, modify details, and save the updates to the server.</p>', unsafe_allow_html=True)

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
        with st.spinner("Loading patient profile..."):
            patient = get_patient_by_id(
                patient_id
            )

        if not patient:
            st.error("Patient not found in the database. Please verify the UUID.")
            return

        patient = patient[0]
        st.session_state["patient"] = patient

    if "patient" in st.session_state:
        patient = st.session_state["patient"]

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>✏️ Modify Patient Information</h4>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            patient_name = st.text_input(
                "Patient Name",
                value=patient.get("patient_name", "")
            )

            gender = st.selectbox(
                "Gender",
                ["Male", "Female", "Other"],
                index=["Male", "Female", "Other"].index(patient.get("gender", "Male"))
            )

            age = st.number_input(
                "Age",
                min_value=0,
                max_value=120,
                value=int(patient.get("age", 0))
            )

        with col2:
            phone_number = st.text_input(
                "Phone Number",
                value=patient.get("phone_number", "")
            )

            disease = st.text_input(
                "Disease / Complaint",
                value=patient.get("disease", "") or ""
            )

            occupation = st.text_input(
                "Occupation",
                value=patient.get("occupation", "") or ""
            )
        
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button(

            "Update Patient"
        ):

            updated_data = {

                "patient_name":
                    patient_name,

                "gender":
                    gender,

                "age":
                    age,

                "phone_number":
                    phone_number,

                "disease":
                    disease,

                "occupation":
                    occupation
            }

            with st.spinner("Updating patient..."):
                result = update_patient(
                    patient_id,
                    updated_data
                )

            if result:

                st.success(
                    "Patient updated successfully!"
                )

            else:

                st.error(
                    "Update failed"
                )