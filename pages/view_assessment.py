import streamlit as st
import pandas as pd

from services.pain_assessment_crud import (
    get_all_assessments
)


def show_view_assessment_page():

    st.header("View Assessments")

    assessments = (
        get_all_assessments()
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

        st.info(
            "No assessments found."
        )