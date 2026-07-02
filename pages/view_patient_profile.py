import streamlit as st

from services.patient_crud import (
    get_patient_by_id
)

from services.pain_assessment_crud import (
    search_assessment_by_patient_id
)

from services.consultation_crud import (
    search_consultations
)

from services.treatment_crud import (
    search_treatments
)

from services.progress_crud import (
    search_progress
)

from services.conversation_crud import (
    search_conversations
)

from services.ai_crud import (
    get_analysis_by_conversation
)


def show_view_patient_profile_page():

    st.markdown(
        '<h2 class="gradient-header">Patient Profile Dashboard</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="color:#64748b;">
        View a patient's complete medical history by combining
        data from all healthcare modules.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="custom-card">',
        unsafe_allow_html=True
    )

    patient_id = st.text_input(
        "Patient ID",
        placeholder="Enter Patient ID..."
    )

    load_profile = st.button(
        "Load Patient Profile"
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    if load_profile:

        if not patient_id.strip():
            st.warning("Please enter a Patient ID.")
            return

        patient = get_patient_by_id(patient_id.strip())

        if not patient:
            st.error("Patient not found.")
            return

        patient = patient[0]
        
        # Initialize variables to avoid NameError downstream
        consultation = None
        treatment = None
        conversation = None
        consultation_id = None

        # ==================================================
        # PATIENT INFORMATION
        # ==================================================

        st.markdown("---")
        st.subheader("👤 Patient Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Patient Name:** {patient.get('patient_name')}")
            st.write(f"**Patient ID:** {patient.get('patient_id')}")
            st.write(f"**Age:** {patient.get('age')}")
            st.write(f"**Gender:** {patient.get('gender')}")
            st.write(f"**Phone Number:** {patient.get('phone_number')}")

        with col2:
            st.write(f"**Email:** {patient.get('email') or 'N/A'}")
            st.write(f"**Disease:** {patient.get('disease') or 'N/A'}")
            st.write(f"**BMI:** {patient.get('bmi') or 'N/A'}")
            st.write(f"**BMI Category:** {patient.get('bmi_category') or 'N/A'}")
            st.write(f"**Occupation:** {patient.get('occupation') or 'N/A'}")

        st.write(f"**Address:** {patient.get('address') or 'N/A'}")

        if patient.get("previous_spine_injury"):
            st.info(f"Previous Spine Injury: {patient.get('previous_spine_injury')}")

        # ==================================================
        # PAIN ASSESSMENT
        # ==================================================

        st.markdown("---")
        st.subheader("🩺 Pain Assessment")

        assessments = search_assessment_by_patient_id(patient.get("patient_id"))

        if not assessments:
            st.info("No pain assessment found.")
        else:
            assessment = assessments[0]
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Pain Areas:** {assessment.get('pain_areas') or 'N/A'}")
                st.write(f"**Pain Severity:** {assessment.get('pain_severity') or 'N/A'}")

            with col2:
                st.write(f"**Posture:** {assessment.get('posture') or 'N/A'}")
                st.write(f"**Assessment Date:** {assessment.get('created_at') or 'N/A'}")

            if assessment.get("notes"):
                st.info(assessment.get("notes"))

        # ==================================================
        # CONSULTATION
        # ==================================================

        st.markdown("---")
        st.subheader("👨‍⚕️ Consultation")

        consultations = search_consultations(patient_id=patient.get("patient_id"))

        if not consultations:
            st.info("No consultation record found.")
        else:
            consultation = consultations[0]
            consultation_id = consultation.get("consultation_id")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Doctor Name:** {consultation.get('doctor_name')}")
                st.write(f"**Specialization:** {consultation.get('specialization') or 'N/A'}")
                st.write(f"**Consultation Date:** {consultation.get('consultation_date')}")
                st.write(f"**Consultation Time:** {consultation.get('consultation_time') or 'N/A'}")

            with col2:
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

        # ==================================================
        # TREATMENT
        # ==================================================

        st.markdown("---")
        st.subheader("💊 Treatment")

        if consultation:
            treatments = search_treatments(consultation_id=consultation_id)

            if not treatments:
                st.info("No treatment record found.")
            else:
                treatment = treatments[0]
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Treatment Type:** {treatment.get('treatment_type') or 'N/A'}")
                    st.write(f"**Treatment Plan:** {treatment.get('treatment_plan') or 'N/A'}")
                    st.write(f"**Medication:** {treatment.get('medication') or 'N/A'}")
                    st.write(f"**Session Number:** {treatment.get('session_number') or 'N/A'}")

                with col2:
                    st.write(f"**Session Date:** {treatment.get('session_date') or 'N/A'}")
                    st.write(f"**Therapist Name:** {treatment.get('therapist_name') or 'N/A'}")
                    st.write(f"**Treatment Status:** {treatment.get('treatment_status') or 'N/A'}")

                    followup = "Yes" if treatment.get("followup_required") else "No"
                    st.write(f"**Follow-up Required:** {followup}")

                if treatment.get("notes"):
                    st.info(treatment.get("notes"))
        else:
            st.info("Treatment cannot be loaded because no consultation record exists.")

        # ==================================================
        # PROGRESS TRACKING
        # ==================================================

        st.markdown("---")
        st.subheader("📈 Progress Tracking")

        if treatment:
            progress_records = search_progress(
                patient_id=patient.get("patient_id"),
                treatment_id=treatment.get("treatment_id")
            )

            if not progress_records:
                st.info("No progress tracking record found.")
            else:
                progress = progress_records[0]
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Session Number:** {progress.get('session_number')}")
                    st.write(f"**Progress Date:** {progress.get('progress_date')}")
                    st.write(f"**Previous Pain Score:** {progress.get('previous_pain_score')}")
                    st.write(f"**Current Pain Score:** {progress.get('current_pain_score')}")
                    st.write(f"**Recovery Status:** {progress.get('overall_recovery_status') or 'N/A'}")

                with col2:
                    st.write(f"**Mobility Improvement:** {progress.get('mobility_improvement')}%")
                    st.write(f"**Sleep Quality:** {progress.get('sleep_quality')}/10")
                    st.write(f"**Numbness Improvement:** {progress.get('numbness_improvement')}%")
                    st.write(f"**Range of Motion:** {progress.get('range_of_motion')}%")

                if progress.get("patient_feedback"):
                    st.success(f"**Patient Feedback:** {progress.get('patient_feedback')}")

                if progress.get("practitioner_remark"):
                    st.info(f"**Practitioner Remark:** {progress.get('practitioner_remark')}")
        else:
            st.info("Progress tracking cannot be loaded because no treatment record exists.")

        # ==================================================
        # CONVERSATION HISTORY
        # ==================================================

        st.markdown("---")
        st.subheader("🎙️ Conversation History")

        if consultation:
            conversations = search_conversations(consultation_id=consultation_id)

            if not conversations:
                st.info("No conversation record found.")
            else:
                conversation = conversations[0]

                conversation_id = conversation.get(
                    "conversation_id"
                )
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Source:** {conversation.get('source') or 'N/A'}")
                    st.write(f"**Language:** {conversation.get('language') or 'N/A'}")
                    st.write(f"**Emotion Detected:** {conversation.get('emotional_state') or 'N/A'}")

                with col2:
                    st.write(f"**Pain Keywords:** {conversation.get('pain_keywords') or 'N/A'}")
                    st.write(f"**Created At:** {conversation.get('created_at') or 'N/A'}")

                st.markdown("#### Transcript")
                st.write(conversation.get("raw_transcript") or "N/A")

                if conversation.get("speaker_separation"):
                    st.markdown("#### Speaker Separation")
                    st.write(conversation.get("speaker_separation"))

                if conversation.get("additional_notes"):
                    st.info(conversation.get("additional_notes"))
        else:
            st.info("Conversation cannot be loaded because no consultation record exists.")

        # ==================================================
        # AI ANALYSIS
        # ==================================================

        st.markdown("---")
        st.subheader("🤖 AI Analysis")

        if conversation:
            analysis = get_analysis_by_conversation(conversation_id)

            if not analysis:
                st.info("No AI analysis available.")
            else:
                analysis = analysis[0]
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Risk Level:** {analysis.get('risk_level') or 'N/A'}")
                    st.write(f"**Emotional State:** {analysis.get('emotional_state') or 'N/A'}")
                    st.write(f"**Recovery Prediction:** {analysis.get('recovery_prediction') or 'N/A'}")
                    st.write(f"**AI Confidence:** {analysis.get('ai_confidence') or 'N/A'}")

                with col2:
                    st.write(f"**Surgery Probability:** {analysis.get('surgery_probability') or 'N/A'}")
                    st.write(f"**Pain Keywords:** {analysis.get('pain_keywords') or 'N/A'}")
                    st.write(f"**Created At:** {analysis.get('created_at') or 'N/A'}")

                st.markdown("#### Summary")
                st.write(analysis.get("summary") or "N/A")

                st.markdown("#### Extracted Symptoms")
                st.write(analysis.get("extracted_symptoms") or "N/A")

                st.markdown("#### Recommendations")
                st.write(analysis.get("recommendations") or "N/A")

                if analysis.get("transcript"):
                    with st.expander("View AI Transcript"):
                        st.write(analysis.get("transcript"))
        else:
            st.info("AI analysis cannot be loaded because no conversation record exists.")