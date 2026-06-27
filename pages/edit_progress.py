import streamlit as st

from services.progress_crud import (
    get_progress_by_id,
    update_progress
)


def show_edit_progress_page():

    st.markdown(
        '<h2 class="gradient-header">Edit Progress Record</h2>',
        unsafe_allow_html=True
    )

    progress_id = st.text_input(
        "Progress ID"
    )

    if not progress_id:
        return

    try:

        progress = get_progress_by_id(
            progress_id.strip()
        )

        if not progress:

            st.warning(
                "Progress record not found."
            )

            return

        st.markdown(
            '<div class="custom-card">',
            unsafe_allow_html=True
        )

        session_number = st.number_input(

            "Session Number",

            min_value=1,

            value=progress["session_number"]

        )

        previous_pain_score = st.slider(

            "Previous Pain Score",

            0,

            10,

            progress["previous_pain_score"]

        )

        current_pain_score = st.slider(

            "Current Pain Score",

            0,

            10,

            progress["current_pain_score"]

        )

        mobility_improvement = st.slider(

            "Mobility Improvement (%)",

            0,

            100,

            progress["mobility_improvement"]

        )

        sleep_quality = st.slider(

            "Sleep Quality",

            0,

            10,

            progress["sleep_quality"]

        )

        numbness_improvement = st.slider(

            "Numbness Improvement (%)",

            0,

            100,

            progress["numbness_improvement"]

        )

        range_of_motion = st.slider(

            "Range of Motion Improvement (%)",

            0,

            100,

            progress["range_of_motion"]

        )

        patient_feedback = st.text_area(

            "Patient Feedback",

            value=progress["patient_feedback"]

        )

        practitioner_remark = st.text_area(

            "Practitioner Remark",

            value=progress["practitioner_remark"]

        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if st.button(

            "Update Progress"

        ):

            updated_data = {

                "session_number": session_number,

                "previous_pain_score": previous_pain_score,

                "current_pain_score": current_pain_score,

                "mobility_improvement": mobility_improvement,

                "sleep_quality": sleep_quality,

                "numbness_improvement": numbness_improvement,

                "range_of_motion": range_of_motion,

                "patient_feedback": patient_feedback,

                "practitioner_remark": practitioner_remark

            }

            update_progress(

                progress_id,

                updated_data

            )

            st.success(

                "Progress updated successfully."

            )

    except Exception as exc:

        st.error(

            f"{type(exc).__name__}: {exc}"

        )