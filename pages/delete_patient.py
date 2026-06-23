import streamlit as st

from services.patient_crud import (
    get_patient_by_id,
    delete_patient
)


def show_delete_patient_page():

    st.header("Delete Patient")

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

        st.session_state["delete_patient"] = (
            patient[0]
        )

    if "delete_patient" in st.session_state:

        patient = (
            st.session_state[
                "delete_patient"
            ]
        )

        st.subheader(
            "Patient Details"
        )

        st.write(
            f"Name: {patient['patient_name']}"
        )

        st.write(
            f"Gender: {patient['gender']}"
        )

        st.write(
            f"Age: {patient['age']}"
        )

        st.write(
            f"Phone: {patient['phone_number']}"
        )

        st.warning(
            "This action cannot be undone."
        )

        confirm = st.checkbox("I confirm deletion")

        if confirm and st.button("Delete Patient"):

            result = delete_patient(
                patient["patient_id"]
            )

            if result:

                st.success(
                    "Patient deleted successfully!"
                )

                del st.session_state[
                    "delete_patient"
                ]

            else:

                st.error(
                    "Delete failed"
                )