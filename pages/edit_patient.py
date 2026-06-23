import streamlit as st

from services.patient_crud import (
    get_patient_by_id,
    update_patient
)


def show_edit_patient_page():

    st.header("Edit Patient")

    patient_id = st.text_input(
        "Enter Patient UUID"
    )

    if st.button("Load Patient"):

        patient = get_patient_by_id(
            patient_id
        )

        if not patient:

            st.error(
                "Patient not found"
            )
            return

        patient = patient[0]

        st.session_state["patient"] = (
            patient
        )

    if "patient" in st.session_state:

        patient = (
            st.session_state["patient"]
        )

        st.subheader(
            "Patient Details"
        )

        patient_name = st.text_input(
            "Patient Name",
            value=patient.get(
                "patient_name",
                ""
            )
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"],
            index=[
                "Male",
                "Female",
                "Other"
            ].index(
                patient.get(
                    "gender",
                    "Male"
                )
            )
        )

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            value=int(
                patient.get(
                    "age",
                    0
                )
            )
        )

        phone_number = st.text_input(
            "Phone Number",
            value=patient.get(
                "phone_number",
                ""
            )
        )

        disease = st.text_input(
            "Disease",
            value=patient.get(
                "disease",
                ""
            ) or ""
        )

        occupation = st.text_input(
            "Occupation",
            value=patient.get(
                "occupation",
                ""
            ) or ""
        )

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