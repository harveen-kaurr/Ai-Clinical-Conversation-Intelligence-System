import streamlit as st

from services.progress_crud import create_progress
from services.progress_service import ProgressService


def show_add_progress_page():

    st.markdown(
        '<h2 class="gradient-header">Patient Progress Tracking</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom:20px;">'
        'Track recovery progress, compare pain scores and monitor patient improvements.'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="custom-card">',
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(

        [
            "📈 Recovery Metrics",
            "📝 Feedback"
        ]

    )

    with tab1:

        st.markdown(
            "<h4 style='color:#1e3a8a;'>Recovery Information</h4>",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            patient_id = st.text_input(

                "Patient ID (UUID) *"

            )

            treatment_id = st.text_input(

                "Treatment ID (UUID) *"

            )

            session_number = st.number_input(

                "Session Number",

                min_value=1,

                value=1

            )

            progress_date = st.date_input(

                "Progress Date"

            )

            previous_pain_score = st.slider(

                "Previous Pain Score",

                0,

                10,

                5

            )

            current_pain_score = st.slider(

                "Current Pain Score",

                0,

                10,

                3

            )

        with col2:

            mobility_improvement = st.slider(

                "Mobility Improvement (%)",

                0,

                100,

                50

            )

            sleep_quality = st.slider(

                "Sleep Quality",

                0,

                10,

                5

            )

            numbness_improvement = st.slider(

                "Numbness Improvement (%)",

                0,

                100,

                50

            )

            range_of_motion = st.slider(

                "Range of Motion Improvement (%)",

                0,

                100,

                50

            )

    with tab2:

        st.markdown(

            "<h4 style='color:#0d9488;'>Patient Feedback</h4>",

            unsafe_allow_html=True

        )

        patient_feedback = st.text_area(

            "Patient Feedback",

            height=120

        )

        practitioner_remark = st.text_area(

            "Practitioner Remark",

            height=120

        )

    st.markdown(

        "</div>",

        unsafe_allow_html=True

    )

    submit = st.button(

        "Save Progress"

    )

    if submit:

        progress_data = {

            "patient_id": patient_id.strip(),

            "treatment_id": treatment_id.strip(),

            "session_number": session_number,

            "progress_date": progress_date,

            "previous_pain_score": previous_pain_score,

            "current_pain_score": current_pain_score,

            "mobility_improvement": mobility_improvement,

            "sleep_quality": sleep_quality,

            "numbness_improvement": numbness_improvement,

            "range_of_motion": range_of_motion,

            "patient_feedback": patient_feedback,

            "practitioner_remark": practitioner_remark

        }

        try:

            payload = ProgressService.register_progress(

                progress_data

            )

            with st.spinner(

                "Saving progress..."

            ):

                created_progress = create_progress(

                    payload

                )

            if created_progress:

                st.success(

                    "Progress record added successfully."

                )

                st.json(

                    created_progress[0]

                )

            else:

                st.error(

                    "Unable to save progress."

                )

        except Exception as exc:

            st.error(

                f"{type(exc).__name__}: {exc}"

            )