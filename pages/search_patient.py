import streamlit as st
import pandas as pd

from services.patient_crud import (
    search_patient_by_name,
    search_patient_by_phone,
    search_patient_by_patient_id,
    search_patient_by_disease,
    get_patient_by_id
)

from services.pain_assessment_crud import (
    search_assessment_by_pain_area
)

from services.consultation_crud import (
    search_consultation_by_id
)


def show_search_patient_page():

    st.markdown(
        '<h2 class="gradient-header">Search Patient Records</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Lookup patient accounts in the database by Name, Phone Number, Patient ID, Disease, Pain Area, or Consultation ID.</p>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

    search_col1, search_col2 = st.columns([1, 2])

    with search_col1:
        search_type = st.selectbox(
            "Search Parameter",
            [
                "Patient Name",
                "Phone Number",
                "Patient ID",
                "Disease",
                "Pain Area",
                "Consultation ID"
            ]
        )

    with search_col2:
        search_value = st.text_input(
            "Enter Search Term",
            placeholder=f"Enter {search_type.lower()}..."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### Additional Filters")

    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        gender_filter = st.selectbox(
            "Gender",
            ["All", "Male", "Female", "Other"]
        )

    with filter_col2:
        age_filter = st.number_input(
            "Age",
            min_value=0,
            value=0
        )

    with filter_col3:
        visit_date = st.date_input(
            "Visit Date",
            value=None
        )

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Search Database"):

        if not search_value.strip():
            st.warning("Please enter a search query.")
            return

        with st.spinner("Searching records..."):

            if search_type == "Patient Name":
                results = search_patient_by_name(search_value)

            elif search_type == "Phone Number":
                results = search_patient_by_phone(search_value)

            elif search_type == "Patient ID":
                results = search_patient_by_patient_id(search_value)

            elif search_type == "Disease":
                results = search_patient_by_disease(search_value)

            elif search_type == "Pain Area":

                assessments = search_assessment_by_pain_area(search_value)

                results = []

                for assessment in assessments:
                    patient = get_patient_by_id(
                        assessment["patient_id"]
                    )

                    if patient:
                        results.extend(patient)

            elif search_type == "Consultation ID":

                consultations = search_consultation_by_id(
                    search_value
                )

                results = []

                for consultation in consultations:
                    patient = get_patient_by_id(
                        consultation["patient_id"]
                    )

                    if patient:
                        results.extend(patient)

            else:
                results = []

        # ---------------- APPLY FILTERS ----------------

        filtered_results = []

        for patient in results:

            # Gender Filter
            if (
                gender_filter != "All"
                and patient.get("gender") != gender_filter
            ):
                continue

            # Age Filter
            if (
                age_filter != 0
                and patient.get("age") != age_filter
            ):
                continue

            # Visit Date Filter
            if (
                visit_date
                and str(patient.get("date_of_visiting")) != str(visit_date)
            ):
                continue

            filtered_results.append(patient)

        results = filtered_results

        # -----------------------------------------------

        if not results:
            st.error("No matching patient record found in the database.")
            return

        st.success(f"Found {len(results)} matching patient account(s).")

        for patient in results:

            with st.container():

                st.markdown("---")

                st.subheader(f"👤 {patient.get('patient_name')}")

                col1, col2 = st.columns(2)

                with col1:

                    st.write(f"**Patient ID:** {patient.get('patient_id')}")
                    st.write(f"**Age:** {patient.get('age')}")
                    st.write(f"**Gender:** {patient.get('gender')}")
                    st.write(f"**Phone:** {patient.get('phone_number')}")
                    st.write(f"**Email:** {patient.get('email') or 'N/A'}")

                with col2:

                    st.write(f"**Disease:** {patient.get('disease') or 'N/A'}")
                    st.write(f"**Date of Visiting:** {patient.get('date_of_visiting') or 'N/A'}")
                    st.write(
                        f"**BMI:** {patient.get('bmi') or 'N/A'} "
                        f"({patient.get('bmi_category') or 'N/A'})"
                    )
                    st.write(
                        f"**Emergency Contact:** {patient.get('emergency_contact') or 'N/A'}"
                    )

                if patient.get("previous_spine_injury"):

                    st.info(
                        f"Previous Spine Injury: {patient.get('previous_spine_injury')}"
                    )