import streamlit as st

from services.consultation_service import (
    ConsultationService
)

from services.consultation_crud import (
    create_consultation
)

from services.file_service import FileService



def show_add_consultation_page():

    st.markdown('<h2 class="gradient-header">Add Clinical Consultation</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Log doctor consultations, record full physical examination notes, and establish preliminary diagnoses.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    # Establish EHR Workflow tabs
    tab_info, tab_exams, tab_diagnosis = st.tabs([
        "📋 1. Consultation Info",
        "🩺 2. Clinical Examinations",
        "🧠 3. Diagnosis & Follow-up"
    ])

    with tab_info:
        st.markdown("<h4 style='color:#1e3a8a; margin-top:10px; margin-bottom:15px;'>General consultation records</h4>", unsafe_allow_html=True)
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
        with col2:
            consultation_date = st.date_input(
                "Consultation Date *"
            )
            consultation_time = st.time_input(
                "Consultation Time *"
            )

        chief_complaint = st.text_area(
            "Chief Complaint *",
            placeholder="What is the patient experiencing? (e.g. chronic lower back pain shooting to knee)",
            height=100
        )

    with tab_exams:
        st.markdown("<h4 style='color:#0d9488; margin-top:10px; margin-bottom:15px;'>Systematic clinical examinations</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            spine_exam = st.text_area(
                "Spine Examination (Range of motion, curvature...)",
                height=80
            )
            muscle_exam = st.text_area(
                "Muscle Examination (Tone, strength...)",
                height=80
            )
            nerve_exam = st.text_area(
                "Nerve Examination (Reflexes, sensitivity...)",
                height=80
            )
        with col2:
            tissue_exam = st.text_area(
                "Tissue Examination (Skin, subcutaneous...)",
                height=80
            )
            bone_joint_exam = st.text_area(
                "Bone & Joint Examination (Swelling, tenderness...)",
                height=80
            )

    with tab_diagnosis:
        st.markdown("<h4 style='color:#1e3a8a; margin-top:10px; margin-bottom:15px;'>Diagnostic assessment & next steps</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            clinical_findings = st.text_area(
                "Clinical Findings Summary",
                height=100
            )
            preliminary_diagnosis = st.text_area(
                "Preliminary Diagnosis",
                height=100
            )
        with col2:
            recommended_scan = st.text_input(
                "Recommended Scan (e.g. MRI, X-Ray)"
            )
            followup_date = st.date_input(
                "Follow-up Date"
            )
            uploaded_file = st.file_uploader(
                "Upload Scans / Reports (PDF, PNG, JPG)",
                type=["pdf", "png", "jpg", "jpeg"]
            )

    st.markdown('</div>', unsafe_allow_html=True)

    submit = st.button(
        "Save Consultation"
    )

    if submit:

        try:

            consultation_data = {
                "patient_id": patient_id.strip(),
                "doctor_name": doctor_name.strip(),
                "specialization": specialization.strip(),
                "consultation_date": str(consultation_date),
                "consultation_time": str(consultation_time),
                "chief_complaint": chief_complaint.strip(),
                "clinical_findings": clinical_findings.strip() if clinical_findings.strip() else None,
                "spine_exam": spine_exam.strip() if spine_exam.strip() else None,
                "muscle_exam": muscle_exam.strip() if muscle_exam.strip() else None,
                "nerve_exam": nerve_exam.strip() if nerve_exam.strip() else None,
                "tissue_exam": tissue_exam.strip() if tissue_exam.strip() else None,
                "bone_joint_exam": bone_joint_exam.strip() if bone_joint_exam.strip() else None,
                "preliminary_diagnosis": preliminary_diagnosis.strip() if preliminary_diagnosis.strip() else None,
                "recommended_scan": recommended_scan.strip() if recommended_scan.strip() else None,
                "followup_date": str(followup_date) if followup_date else None
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
                consultation_id = created_consultation[0].get("consultation_id")
                
                # Perform File Upload if present
                uploaded_metadata = None
                if uploaded_file is not None:
                    with st.spinner("Uploading report file..."):
                        uploaded_metadata = FileService.upload_file(
                            consultation_id=consultation_id,
                            uploaded_file=uploaded_file,
                            file_type="MRI/X-Ray"
                        )

                st.success("Consultation saved successfully!")
                
                # Display final summary card
                st.json(created_consultation[0])
                if uploaded_metadata:
                    st.info(f"File uploaded successfully! URL: {uploaded_metadata.get('file_url')}")
            else:
                st.error("Failed to save consultation")

        except Exception as exc:
            st.error(f"{type(exc).__name__}: {exc}")