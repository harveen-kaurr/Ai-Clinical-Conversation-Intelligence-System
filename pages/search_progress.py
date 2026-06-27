import streamlit as st
import pandas as pd

from services.progress_crud import search_progress


def show_search_progress_page():

    st.markdown(
        '<h2 class="gradient-header">Search Progress Records</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom:20px;">'
        'Search patient recovery records using Patient ID, Treatment ID or Session Number.'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="custom-card">',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        patient_id = st.text_input(
            "Patient ID"
        )

        treatment_id = st.text_input(
            "Treatment ID"
        )

    with col2:

        session_number = st.number_input(
            "Session Number",
            min_value=0,
            value=0
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    search = st.button(
        "Search Progress"
    )

    if search:

        try:

            records = search_progress(

                patient_id=patient_id.strip() if patient_id else None,

                treatment_id=treatment_id.strip() if treatment_id else None,

                session_number=session_number if session_number > 0 else None

            )

            if not records:

                st.warning(
                    "No matching records found."
                )

                return

            df = pd.DataFrame(records)

            st.success(
                f"{len(df)} record(s) found."
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.markdown("---")

            st.subheader("Record Details")

            selected = st.selectbox(

                "Select Progress Record",

                range(len(records)),

                format_func=lambda x:
                records[x]["progress_id"]

            )

            st.json(

                records[selected]

            )

        except Exception as exc:

            st.error(

                f"{type(exc).__name__}: {exc}"

            )