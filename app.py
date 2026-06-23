import streamlit as st
from pages.view_patients import (
    show_view_patients_page
)
from pages.search_patient import (
    show_search_patient_page
)

from pages.add_patient import (
    show_add_patient_page
)
from pages.edit_patient import (
    show_edit_patient_page
)
from pages.delete_patient import (
    show_delete_patient_page
)

st.set_page_config(
    page_title="AI Clinic",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Add Patient",
        "View Patients",
        "Edit Patient",
        "Delete Patient",
        "Search Patient"
    ]
)

if page == "Add Patient":
    show_add_patient_page()

elif page == "View Patients":
    show_view_patients_page()
elif page == "Search Patient":
    show_search_patient_page()
elif page == "Edit Patient":
    show_edit_patient_page()
elif page == "Delete Patient":
    show_delete_patient_page()
else:
    st.info(
        f"{page} page coming soon"
    )