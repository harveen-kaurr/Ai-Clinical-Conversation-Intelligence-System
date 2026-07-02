# Generated view_patient_profile.py
# (See chat for explanation)

import streamlit as st

from services.patient_crud import get_patient_by_id
from services.pain_assessment_crud import search_assessment_by_patient_id
from services.consultation_crud import search_consultations
from services.treatment_crud import search_treatments


def show_view_patient_profile_page():

    st.markdown('<h2 class="gradient-header">Patient Profile Dashboard</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b;">View a patient\'s complete medical history by combining data from all healthcare modules.</p>', unsafe_allow_html=True)

    patient_id = st.text_input("Patient ID", placeholder="Enter Patient ID...")
    load_profile = st.button("Load Patient Profile")

    if not load_profile:
        return

    if not patient_id.strip():
        st.warning("Please enter a Patient ID.")
        return

    patient = get_patient_by_id(patient_id.strip())
    if not patient:
        st.error("Patient not found.")
        return

    patient = patient[0]

    st.markdown("---")
    st.subheader("👤 Patient Information")
    c1,c2=st.columns(2)
    with c1:
        st.write(f"**Patient Name:** {patient.get('patient_name')}")
        st.write(f"**Patient ID:** {patient.get('patient_id')}")
        st.write(f"**Age:** {patient.get('age')}")
        st.write(f"**Gender:** {patient.get('gender')}")
        st.write(f"**Phone Number:** {patient.get('phone_number')}")
    with c2:
        st.write(f"**Email:** {patient.get('email') or 'N/A'}")
        st.write(f"**Disease:** {patient.get('disease') or 'N/A'}")
        st.write(f"**BMI:** {patient.get('bmi') or 'N/A'}")
        st.write(f"**BMI Category:** {patient.get('bmi_category') or 'N/A'}")
        st.write(f"**Occupation:** {patient.get('occupation') or 'N/A'}")
    st.write(f"**Address:** {patient.get('address') or 'N/A'}")
    if patient.get("previous_spine_injury"):
        st.info(f"Previous Spine Injury: {patient.get('previous_spine_injury')}")

    st.markdown("---")
    st.subheader("🩺 Pain Assessment")
    assessments=search_assessment_by_patient_id(patient.get("patient_id"))
    if not assessments:
        st.info("No pain assessment found.")
    else:
        a=assessments[0]
        c1,c2=st.columns(2)
        with c1:
            st.write(f"**Pain Areas:** {a.get('pain_areas') or 'N/A'}")
            st.write(f"**Pain Severity:** {a.get('pain_severity') or 'N/A'}")
        with c2:
            st.write(f"**Posture:** {a.get('posture') or 'N/A'}")
            st.write(f"**Assessment Date:** {a.get('created_at') or 'N/A'}")
        if a.get("notes"):
            st.info(a.get("notes"))

    st.markdown("---")
    st.subheader("👨‍⚕️ Consultation")
    consultations=search_consultations(patient_id=patient.get("patient_id"))
    consultation=None
    if not consultations:
        st.info("No consultation record found.")
    else:
        consultation=consultations[0]
        c1,c2=st.columns(2)
        with c1:
            st.write(f"**Doctor Name:** {consultation.get('doctor_name')}")
            st.write(f"**Specialization:** {consultation.get('specialization') or 'N/A'}")
            st.write(f"**Consultation Date:** {consultation.get('consultation_date')}")
            st.write(f"**Consultation Time:** {consultation.get('consultation_time') or 'N/A'}")
        with c2:
            st.write(f"**Chief Complaint:** {consultation.get('chief_complaint')}")
            st.write(f"**Preliminary Diagnosis:** {consultation.get('preliminary_diagnosis') or 'N/A'}")
            st.write(f"**Recommended Scan:** {consultation.get('recommended_scan') or 'N/A'}")
            st.write(f"**Follow-up Date:** {consultation.get('follow_up_date') or 'N/A'}")
        st.markdown("#### Clinical Examination")
        st.write(f"**Clinical Findings:** {consultation.get('clinical_findings') or 'N/A'}")
        st.write(f"**Spine Examination:** {consultation.get('spine_examination') or 'N/A'}")
        st.write(f"**Muscle Examination:** {consultation.get('muscle_examination') or 'N/A'}")
        st.write(f"**Nerve Examination:** {consultation.get('nerve_examination') or 'N/A'}")
        st.write(f"**Bone & Joint Examination:** {consultation.get('bone_joint_examination') or 'N/A'}")

    st.markdown("---")
    st.subheader("💊 Treatment")
    if consultation is None:
        st.info("No consultation available to load treatment.")
    else:
        treatments=search_treatments(consultation_id=consultation.get("consultation_id"))
        if not treatments:
            st.info("No treatment record found.")
        else:
            t=treatments[0]
            c1,c2=st.columns(2)
            with c1:
                st.write(f"**Treatment Type:** {t.get('treatment_type') or 'N/A'}")
                st.write(f"**Treatment Plan:** {t.get('treatment_plan') or 'N/A'}")
                st.write(f"**Medication:** {t.get('medication') or 'N/A'}")
                st.write(f"**Session Number:** {t.get('session_number') or 'N/A'}")
            with c2:
                st.write(f"**Session Date:** {t.get('session_date') or 'N/A'}")
                st.write(f"**Therapist Name:** {t.get('therapist_name') or 'N/A'}")
                st.write(f"**Treatment Status:** {t.get('treatment_status') or 'N/A'}")
                st.write(f"**Follow-up Required:** {'Yes' if t.get('followup_required') else 'No'}")
            if t.get("notes"):
                st.info(t.get("notes"))
