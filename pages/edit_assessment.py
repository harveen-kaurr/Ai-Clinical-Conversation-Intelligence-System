import streamlit as st

from services.pain_assessment_crud import (
    get_assessment_by_id,
    update_assessment
)


def show_edit_assessment_page():

    st.header("Edit Assessment")

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
                "assessment"
            ] = assessment[0]

            st.session_state[
                "assessment_id"
            ] = assessment_id

        else:

            st.error(
                "Assessment not found."
            )

    if "assessment" in st.session_state:

        assessment = (
            st.session_state[
                "assessment"
            ]
        )

        pain_areas = st.text_input(
            "Pain Areas",
            value=assessment.get(
                "pain_areas",
                ""
            )
        )

        pain_severity = st.slider(
            "Pain Severity",
            0,
            10,
            int(
                assessment.get(
                    "pain_severity",
                    0
                )
            )
        )

        posture = st.text_input(
            "Posture",
            value=assessment.get(
                "posture",
                ""
            )
        )

        notes = st.text_area(
            "Notes",
            value=assessment.get(
                "notes",
                ""
            )
        )

        if st.button(
            "Update Assessment"
        ):

            updated_data = {

                "pain_areas":
                    pain_areas,

                "pain_severity":
                    pain_severity,

                "posture":
                    posture,

                "notes":
                    notes
            }

            result = (
                update_assessment(
                    st.session_state[
                        "assessment_id"
                    ],
                    updated_data
                )
            )

            st.success(
                "Assessment updated successfully!"
            )

            st.write(
                result
            )

            del st.session_state[
                "assessment"
            ]

            del st.session_state[
                "assessment_id"
            ]