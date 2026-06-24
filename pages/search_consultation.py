import streamlit as st
import pandas as pd

from services.consultation_crud import (
    search_consultations
)


def show_search_consultation_page():

    st.header("Search Consultation")

    patient_id = st.text_input(
        "Patient ID"
    )

    doctor_name = st.text_input(
        "Doctor Name"
    )

    search = st.button(
        "Search"
    )

    if search:

        consultations = (
            search_consultations(
                patient_id=patient_id,
                doctor_name=doctor_name
            )
        )

        if consultations:

            df = pd.DataFrame(
                consultations
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No consultations found."
            )