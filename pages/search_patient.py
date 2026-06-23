import streamlit as st
import pandas as pd

from services.patient_crud import (
    search_patient_by_name,
    search_patient_by_phone,
    search_patient_by_patient_id
)


def show_search_patient_page():

    st.header("Search Patient")

    search_type = st.selectbox(
        "Search By",
        [
            "Patient Name",
            "Phone Number",
            "Patient ID"
        ]
    )

    search_value = st.text_input(
        "Enter Search Value"
    )

    if st.button("Search"):

        if not search_value.strip():

            st.warning(
                "Please enter a value to search."
            )

            return

        with st.spinner("Searching..."):

            if search_type == "Patient Name":

                results = search_patient_by_name(
                    search_value
                )

            elif search_type == "Phone Number":

                results = search_patient_by_phone(
                    search_value
                )

            else:

                results = (
                    search_patient_by_patient_id(
                        search_value
                    )
                )

        if not results:

            st.error(
                "No matching patient found."
            )

            return

        st.success(
            f"{len(results)} record(s) found."
        )

        df = pd.DataFrame(results)

        st.dataframe(
            df,
            use_container_width=True
        )