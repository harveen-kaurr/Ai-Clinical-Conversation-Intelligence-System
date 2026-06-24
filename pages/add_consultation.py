import streamlit as st

from services.consultation_service import (
    ConsultationService
)

from services.consultation_crud import (
    create_consultation
)


def show_add_consultation_page():

    st.header("Add Consultation")

    col1, col2 = st.columns(2)

    with col1:

        patient_id = st.text_input(
            "Patient ID *"
        )

        doctor_name = st.text_input(
            "Doctor Name *"
        )

        specialization = st.text_input(
            "Specialization *"
        )

        consultation_date = st.date_input(
            "Consultation Date *"
        )

        consultation_time = st.time_input(
            "Consultation Time *"
        )

        chief_complaint = st.text_area(
            "Chief Complaint *"
        )

        clinical_findings = st.text_area(
            "Clinical Findings"
        )

    with col2:

        spine_exam = st.text_area(
            "Spine Examination"
        )

        muscle_exam = st.text_area(
            "Muscle Examination"
        )

        nerve_exam = st.text_area(
            "Nerve Examination"
        )

        tissue_exam = st.text_area(
            "Tissue Examination"
        )

        bone_joint_exam = st.text_area(
            "Bone & Joint Examination"
        )

        preliminary_diagnosis = st.text_area(
            "Preliminary Diagnosis"
        )

        recommended_scan = st.text_input(
            "Recommended Scan"
        )

        followup_date = st.date_input(
            "Follow-up Date"
        )

    submit = st.button(
        "Save Consultation"
    )

    if submit:

        try:

            consultation_data = {

                "patient_id":
                    patient_id,

                "doctor_name":
                    doctor_name,

                "specialization":
                    specialization,

                "consultation_date":
                    consultation_date,

                "consultation_time":
                    consultation_time,

                "chief_complaint":
                    chief_complaint,

                "clinical_findings":
                    clinical_findings,

                "spine_exam":
                    spine_exam,

                "muscle_exam":
                    muscle_exam,

                "nerve_exam":
                    nerve_exam,

                "tissue_exam":
                    tissue_exam,

                "bone_joint_exam":
                    bone_joint_exam,

                "preliminary_diagnosis":
                    preliminary_diagnosis,

                "recommended_scan":
                    recommended_scan,

                "followup_date":
                    followup_date
            }

            payload = (
                ConsultationService.register_consultation(
                    consultation_data
                )
            )

            created_consultation = (
                create_consultation(
                    payload
                )
            )

            if created_consultation:

                st.success(
                    "Consultation saved successfully!"
                )

                st.json(
                    created_consultation
                )

            else:

                st.error(
                    "Failed to save consultation"
                )

        except Exception as exc:

            st.error(
                f"{type(exc).__name__}: {exc}"
            )