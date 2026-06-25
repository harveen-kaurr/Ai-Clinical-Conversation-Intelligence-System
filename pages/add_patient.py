import streamlit as st

from database.supabase_client import supabase

from services.patient_service import PatientService

from services.patient_crud import (
    create_patient,
)


def show_add_patient_page():

    st.markdown('<h2 class="gradient-header">Add New Patient</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Complete the form below to register a new patient in the clinical intelligence database.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>📋 Personal & Contact Info</h4>", unsafe_allow_html=True)

        patient_name = st.text_input(
            "Patient Name *"
        )

        gender = st.selectbox(
            "Gender *",
            ["Male", "Female", "Other"]
        )

        age = st.number_input(
            "Age *",
            min_value=0,
            max_value=120,
            step=1
        )

        phone_number = st.text_input(
            "Phone Number *"
        )

        alternate_phone_number = st.text_input(
            "Alternate Phone Number"
        )

        email = st.text_input(
            "Email"
        )

        address = st.text_area(
            "Address",
            height=100
        )

        date_of_birth = st.date_input(
            "Date of Birth"
        )

    with col2:
        st.markdown("<h4 style='color:#0d9488; margin-top:0; border-bottom:2px solid #0d9488; padding-bottom:5px;'>🏥 Clinical & Lifestyle Info</h4>", unsafe_allow_html=True)

        date_of_visiting = st.date_input(
            "Date of Visiting"
        )

        occupation = st.text_input(
            "Occupation"
        )

        disease = st.text_input(
            "Primary Complaint / Disease"
        )

        disease_category = st.text_input(
            "Disease Category"
        )

        subcol1, subcol2 = st.columns(2)
        with subcol1:
            height_cm = st.number_input(
                "Height (cm)",
                min_value=0.0
            )
        with subcol2:
            weight_kg = st.number_input(
                "Weight (kg)",
                min_value=0.0
            )

        emergency_contact = st.text_input(
            "Emergency Contact (Phone)"
        )

        lifestyle = st.text_input(
            "Lifestyle (e.g. Sedentary, Active)"
        )

        smoking_alcohol = st.text_input(
            "Smoking / Alcohol Status"
        )

        previous_spine_injury = st.text_area(
            "Previous Spine Injury / Notes",
            height=100
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

    submit = st.button(
        "Register Patient"
    )


    if submit:

        try:

            patient_data = {

                "patient_name":
                    patient_name.strip(),

                "gender":
                    gender,

                "age":
                    int(age),

                "phone_number":
                    phone_number.strip(),

                "alternate_phone_number":
                    alternate_phone_number.strip()
                    if alternate_phone_number.strip()
                    else None,

                "email":
                    email.strip()
                    if email.strip()
                    else None,

                "address":
                    address.strip()
                    if address.strip()
                    else None,

                "date_of_birth":
                    str(date_of_birth),

                "date_of_visiting":
                    str(date_of_visiting),

                "occupation":
                    occupation.strip()
                    if occupation.strip()
                    else None,

                "disease":
                    disease.strip()
                    if disease.strip()
                    else None,

                "disease_category":
                    disease_category.strip()
                    if disease_category.strip()
                    else None,

                "height_cm":
                    height_cm
                    if height_cm > 0
                    else None,

                "weight_kg":
                    weight_kg
                    if weight_kg > 0
                    else None,

                "emergency_contact":
                    emergency_contact.strip()
                    if emergency_contact.strip()
                    else None,

                "lifestyle":
                    lifestyle.strip()
                    if lifestyle.strip()
                    else None,

                "smoking_alcohol":
                    smoking_alcohol.strip()
                    if smoking_alcohol.strip()
                    else None,

                "previous_spine_injury":
                    previous_spine_injury.strip()
                    if previous_spine_injury.strip()
                    else None
            }

            payload = (
                PatientService.register_patient(
                    patient_data=patient_data,
                    supabase=supabase
                )
            )

            st.subheader(
                "Generated Payload"
            )

            st.json(payload)

            created_patient = (
                create_patient(payload)
            )

            if created_patient is not None:

                st.success(
                    "Patient registered successfully!"
                )

                st.json(
                    created_patient
                )

            else:

                st.error(
                    "Insert failed. No data returned from database."
                )

        except Exception as exc:

            st.error(
                f"{type(exc).__name__}: {exc}"
            )

            st.exception(exc)