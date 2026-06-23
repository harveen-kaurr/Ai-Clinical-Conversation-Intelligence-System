import streamlit as st
import pandas as pd

from services.patient_crud import get_all_patients


def show_view_patients_page():

    st.header("View Patients")

    with st.spinner("Loading patients..."):

        patients = get_all_patients()

    if not patients:

        st.warning(
            "No patients found."
        )

        return

    df = pd.DataFrame(patients)

    st.success(
        f"{len(df)} patients loaded successfully."
    )

    st.dataframe(
        df,
        use_container_width=True
    )