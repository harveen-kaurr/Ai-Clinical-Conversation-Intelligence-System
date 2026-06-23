import streamlit as st

from services.pain_assessment_crud import (
    create_assessment
)


def show_add_assessment_page():

    st.header("Add Assessment")

    patient_id = st.text_input(
        "Patient ID"
    )

    pain_areas = st.multiselect(
        "Pain Areas",
        [
            "Neck",
            "Shoulder",
            "Upper Back",
            "Lower Back",
            "Hip",
            "Knee",
            "Ankle"
        ]
    )

    pain_severity = st.slider(
        "Pain Severity",
        0,
        10,
        5
    )

    posture = st.selectbox(
        "Posture",
        [
            "Normal",
            "Forward Head",
            "Rounded Shoulders",
            "Kyphosis",
            "Lordosis"
        ]
    )

    notes = st.text_area(
        "Notes"
    )

    submit = st.button(
        "Save Assessment"
    )

    if submit:

        assessment_data = {

            "patient_id": patient_id,

            "pain_areas":
                ", ".join(pain_areas),

            "pain_severity":
                pain_severity,

            "posture":
                posture,

            "notes":
                notes
        }

        created_assessment = (
            create_assessment(
                assessment_data
            )
        )

        if created_assessment:

            st.success(
                "Assessment saved successfully!"
            )

            st.json(
                created_assessment
            )

        else:

            st.error(
                "Failed to save assessment"
            )