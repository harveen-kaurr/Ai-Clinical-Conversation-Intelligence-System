import streamlit as st
import pandas as pd

from services.pain_assessment_crud import (
    search_assessment_by_patient_id
)


def show_search_assessment_page():

    st.header("Search Assessment")

    patient_id = st.text_input(
        "Enter Patient ID"
    )

    search = st.button(
        "Search"
    )

    if search:

        assessments = (
            search_assessment_by_patient_id(
                patient_id
            )
        )

        if assessments:

            df = pd.DataFrame(
                assessments
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No assessment found."
            )