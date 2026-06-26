import streamlit as st
import datetime
from services.consultation_crud import (
    get_consultation_by_id,
    update_consultation
)
from services.consultation_service import (
    ConsultationService
)
from services.file_service import FileService

def show_edit_consultation_page():
    st.markdown('<h2 class="gradient-header">Edit Clinical Consultation</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Load an existing clinical consultation record by UUID, modify details, and save the changes to the database.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    load_col1, load_col2 = st.columns([3, 1])
    with load_col1:
        consultation_id = st.text_input(
            "Enter Consultation UUID",
            placeholder="e.g. 12345678-1234-1234-1234-123456789012"
        )
    with load_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        load_btn = st.button("Load Consultation")
    st.markdown('</div>', unsafe_allow_html=True)

    if load_btn:
        if not consultation_id.strip():
            st.error("Please enter a valid Consultation UUID.")
            return

        with st.spinner("Loading consultation details..."):
            consultation = get_consultation_by_id(consultation_id.strip())

        if consultation:
            st.session_state["edit_consultation"] = consultation
            st.session_state["edit_consultation_id"] = consultation_id.strip()
            st.success("Consultation loaded successfully!")
        else:
            st.error("Consultation record not found. Please verify the UUID.")

    if "edit_consultation" in st.session_state:
        consultation = st.session_state["edit_consultation"]
        edit_id = st.session_state["edit_consultation_id"]

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>✏️ Modify Consultation Details (ID: {edit_id})</h4>", unsafe_allow_html=True)

        # Establish tabs for editing
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
                    "Patient ID *",
                    value=consultation.get("patient_id", ""),
                    disabled=True,
                    help="The patient ID is fixed for this consultation record."
                )
                doctor_name = st.text_input(
                    "Doctor Name *",
                    value=consultation.get("doctor_name", "")
                )
                specialization = st.text_input(
                    "Specialization *",
                    value=consultation.get("specialization", "")
                )
            with col2:
                consult_date_val = datetime.date.today()
                if consultation.get("consultation_date"):
                    try:
                        consult_date_val = datetime.date.fromisoformat(str(consultation.get("consultation_date")))
                    except Exception:
                        pass
                
                consult_time_val = datetime.time(10, 0)
                if consultation.get("consultation_time"):
                    try:
                        consult_time_val = datetime.time.fromisoformat(str(consultation.get("consultation_time")))
                    except Exception:
                        pass

                consultation_date = st.date_input(
                    "Consultation Date *",
                    value=consult_date_val
                )
                consultation_time = st.time_input(
                    "Consultation Time *",
                    value=consult_time_val
                )

            chief_complaint = st.text_area(
                "Chief Complaint *",
                value=consultation.get("chief_complaint", "") or "",
                placeholder="What is the patient experiencing? (e.g. chronic lower back pain shooting to knee)",
                height=100
            )

        with tab_exams:
            st.markdown("<h4 style='color:#0d9488; margin-top:10px; margin-bottom:15px;'>Systematic clinical examinations</h4>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                spine_exam = st.text_area(
                    "Spine Examination (Range of motion, curvature...)",
                    value=consultation.get("spine_exam", "") or "",
                    height=80
                )
                muscle_exam = st.text_area(
                    "Muscle Examination (Tone, strength...)",
                    value=consultation.get("muscle_exam", "") or "",
                    height=80
                )
                nerve_exam = st.text_area(
                    "Nerve Examination (Reflexes, sensitivity...)",
                    value=consultation.get("nerve_exam", "") or "",
                    height=80
                )
            with col2:
                tissue_exam = st.text_area(
                    "Tissue Examination (Skin, subcutaneous...)",
                    value=consultation.get("tissue_exam", "") or "",
                    height=80
                )
                bone_joint_exam = st.text_area(
                    "Bone & Joint Examination (Swelling, tenderness...)",
                    value=consultation.get("bone_joint_exam", "") or "",
                    height=80
                )

        with tab_diagnosis:
            st.markdown("<h4 style='color:#1e3a8a; margin-top:10px; margin-bottom:15px;'>Diagnostic assessment & next steps</h4>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                clinical_findings = st.text_area(
                    "Clinical Findings Summary",
                    value=consultation.get("clinical_findings", "") or "",
                    height=100
                )
                preliminary_diagnosis = st.text_area(
                    "Preliminary Diagnosis",
                    value=consultation.get("preliminary_diagnosis", "") or "",
                    height=100
                )
            with col2:
                recommended_scan = st.text_input(
                    "Recommended Scan (e.g. MRI, X-Ray)",
                    value=consultation.get("recommended_scan", "") or ""
                )

                followup_date_val = datetime.date.today()
                if consultation.get("followup_date"):
                    try:
                        followup_date_val = datetime.date.fromisoformat(str(consultation.get("followup_date")))
                    except Exception:
                        pass
                
                followup_date = st.date_input(
                    "Follow-up Date",
                    value=followup_date_val
                )
                
                uploaded_file = st.file_uploader(
                    "Upload New Scans / Reports (PDF, PNG, JPG)",
                    type=["pdf", "png", "jpg", "jpeg"]
                )

        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Update Consultation"):
            try:
                updated_data = {
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

                # Validate data using existing ConsultationService validation
                ConsultationService.validate_consultation(updated_data)

                with st.spinner("Updating consultation session..."):
                    result = update_consultation(edit_id, updated_data)
                    
                    if result:
                        # Perform File Upload if present
                        uploaded_metadata = None
                        if uploaded_file is not None:
                            uploaded_metadata = FileService.upload_file(
                                consultation_id=edit_id,
                                uploaded_file=uploaded_file,
                                file_type="MRI/X-Ray"
                            )

                        st.success("Consultation updated successfully!")
                        st.json(result[0])
                        if uploaded_metadata:
                            st.info(f"File uploaded successfully! URL: {uploaded_metadata.get('file_url')}")

                        # Clean session state so page reloads clean
                        del st.session_state["edit_consultation"]
                        del st.session_state["edit_consultation_id"]
                    else:
                        st.error("Failed to update consultation in the database.")
            except Exception as exc:
                st.error(f"{type(exc).__name__}: {exc}")
