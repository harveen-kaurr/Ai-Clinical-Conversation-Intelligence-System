import streamlit as st
import pandas as pd

from services.consultation_crud import (
    get_all_consultations
)


def show_view_consultation_page():

    st.header("View Consultations")

    consultations = (
        get_all_consultations()
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

        st.info(
            "No consultations found."
        )