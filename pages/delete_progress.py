import streamlit as st

from services.progress_crud import (
    get_progress_by_id,
    delete_progress
)


def show_delete_progress_page():

    st.markdown(
        '<h2 class="gradient-header">Delete Progress Record</h2>',
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

        st.markdown("### Record Preview")

        st.json(progress)

        confirm = st.checkbox(
            "I understand this action cannot be undone."
        )

        if confirm:

            if st.button(

                "Delete Progress Record"

            ):

                delete_progress(
                    progress_id
                )

                st.success(
                    "Progress record deleted successfully."
                )

    except Exception as exc:

        st.error(
            f"{type(exc).__name__}: {exc}"
        )