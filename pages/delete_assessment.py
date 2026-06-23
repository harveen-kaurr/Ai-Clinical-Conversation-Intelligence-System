import streamlit as st
import pandas as pd

from services.pain_assessment_crud import (
    get_assessment_by_id,
    delete_assessment
)


def show_delete_assessment_page():

    st.header("Delete Assessment")

    assessment_id = st.text_input(
        "Assessment ID"
    )

    if st.button(
        "Load Assessment"
    ):

        assessment = (
            get_assessment_by_id(
                assessment_id
            )
        )

        if assessment:

            st.session_state[
                "delete_assessment"
            ] = assessment[0]

            st.session_state[
                "delete_assessment_id"
            ] = assessment_id

        else:

            st.error(
                "Assessment not found."
            )

    if "delete_assessment" in st.session_state:

        assessment = (
            st.session_state[
                "delete_assessment"
            ]
        )

        st.subheader(
            "Assessment Details"
        )

        df = pd.DataFrame(
            [assessment]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        if st.button(
            "Confirm Delete"
        ):

            result = (
                delete_assessment(
                    st.session_state[
                        "delete_assessment_id"
                    ]
                )
            )

            st.success(
                "Assessment deleted successfully!"
            )

            st.write(
                result
            )

            del st.session_state[
                "delete_assessment"
            ]

            del st.session_state[
                "delete_assessment_id"
            ]