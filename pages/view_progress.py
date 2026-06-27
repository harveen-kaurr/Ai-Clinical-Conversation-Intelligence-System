import streamlit as st
import pandas as pd

from services.progress_crud import get_all_progress


def show_view_progress_page():

    st.markdown(
        '<h2 class="gradient-header">Patient Progress History</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom:20px;">'
        'View all recorded patient recovery sessions and monitor progress over time.'
        '</p>',
        unsafe_allow_html=True
    )

    try:

        progress_records = get_all_progress()

        if not progress_records:

            st.info(
                "No progress records found."
            )

            return

        df = pd.DataFrame(progress_records)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        st.subheader("Progress Summary")

        total_records = len(df)

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Records",
                total_records
            )

        with col2:

            latest_status = df.iloc[0][
                "overall_recovery_status"
            ]

            st.metric(
                "Latest Recovery Status",
                latest_status
            )

        with col3:

            avg_pain = round(
                df["current_pain_score"].mean(),
                2
            )

            st.metric(
                "Average Current Pain",
                avg_pain
            )

        with st.expander(
            "Latest Progress Record"
        ):

            st.json(
                progress_records[0]
            )

    except Exception as exc:

        st.error(
            f"{type(exc).__name__}: {exc}"
        )