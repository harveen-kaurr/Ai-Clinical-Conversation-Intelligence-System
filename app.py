import streamlit as st

from pages.add_patient import (
    show_add_patient_page
)

from pages.view_patients import (
    show_view_patients_page
)

from pages.search_patient import (
    show_search_patient_page
)

from pages.edit_patient import (
    show_edit_patient_page
)

from pages.delete_patient import (
    show_delete_patient_page
)

from pages.add_assessment import (
    show_add_assessment_page
)

from pages.view_assessment import (
    show_view_assessment_page
)

from pages.search_assessment import (
    show_search_assessment_page
)

from pages.edit_assessment import (
    show_edit_assessment_page
)

from pages.delete_assessment import (
    show_delete_assessment_page
)

from pages.add_consultation import (
    show_add_consultation_page
)

from pages.view_consultation import (
    show_view_consultation_page
)

from pages.search_consultation import (
    show_search_consultation_page
)

st.set_page_config(
    page_title="AI Clinical Intelligence System",
    layout="wide"
)

st.title("🏥 AI Clinical Intelligence System")

st.sidebar.title("Navigation")

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Patient Management",
        "Pain Assessment",
        "Consultation Management"
    ]
)

if module == "Patient Management":

    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Patient",
            "View Patients",
            "Search Patient",
            "Edit Patient",
            "Delete Patient"
        ]
    )

elif module == "Pain Assessment":

    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Assessment",
            "View Assessment",
            "Search Assessment",
            "Edit Assessment",
            "Delete Assessment"
        ]
    )

else:

    page = st.sidebar.radio(
        "Select Action",
        [
            "Add Consultation",
            "View Consultation",
            "Search Consultation"
        ]
    )
# Patient Pages

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

# Assessment Pages

elif page == "Add Assessment":

    show_add_assessment_page()

elif page == "View Assessment":

    show_view_assessment_page()

elif page == "Search Assessment":

    show_search_assessment_page()

elif page == "Edit Assessment":

    show_edit_assessment_page()

elif page == "Delete Assessment":

    show_delete_assessment_page()

#Consultation Page    

elif page == "Add Consultation":

    show_add_consultation_page() 

elif page == "View Consultation":

    show_view_consultation_page()  

elif page == "Search Consultation":

    show_search_consultation_page()         