import streamlit as st
from services.treatment_crud import create_treatment
from services.treatment_service import TreatmentService

def show_add_treatment_page():
    st.markdown('<h2 class="gradient-header">Log Treatment Session</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Record clinical therapies, physical adjustments, Ayurvedic procedures, and home instructions prescribed for a patient\'s consultation visit.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    tab_chiro_physio, tab_ayur_panch, tab_outcome = st.tabs([
        "🩺 Chiropractic & Physio",
        "🍃 Ayurveda & Panchakarma",
        "🎯 Outcome & Exercises"
    ])

    with tab_chiro_physio:
        st.markdown("<h4 style='color:#1e3a8a; margin-top:10px; margin-bottom:15px;'>Chiropractic & Physical Therapies</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            consultation_id = st.text_input(
                "Consultation ID (UUID) *"
            )
            therapy_type = st.multiselect(
                "Therapy Type *",
                [
                    "Chiropractic Adjustment",
                    "Soft Tissue Therapy",
                    "Osteopathy handling",
                    "Ayurveda & Panchakarma",
                    "Spine Decompression",
                    "Nerve flossing",
                    "Bone Alignment"
                ]
            )
            chiropractic_adjustment_area = st.text_input(
                "Chiropractic Adjustment Area (e.g. C5-C6, L4-L5)"
            )
        with col2:
            soft_tissue_therapy = st.text_area(
                "Soft Tissue Therapy details",
                height=80
            )
            nerve_handling_technique = st.text_area(
                "Nerve Handling Technique",
                height=80
            )
            muscle_therapy = st.text_area(
                "Muscle Therapy / Strengthening Exercises",
                height=80
            )

    with tab_ayur_panch:
        st.markdown("<h4 style='color:#0d9488; margin-top:10px; margin-bottom:15px;'>Ayurveda & Panchakarma Treatments</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            ayur_medicine = st.text_area(
                "Prescribed Ayurveda Medicines",
                height=80
            )
            panchakarma_type = st.selectbox(
                "Panchakarma Type",
                [
                    "None",
                    "Abhyanga (Oil Massage)",
                    "Swedana (Steam Therapy)",
                    "Elakizhi (Leaf Bolus)",
                    "Greeva Basti (Cervical)",
                    "Kati Basti (Lumbar)",
                    "Janu Basti (Knee)",
                    "Nasyam",
                    "Vamanam",
                    "Virechanam"
                ]
            )
        with col2:
            oil_used = st.text_input(
                "Medicinal Oils Used (e.g. Mahanarayan Oil)"
            )
            bone_alignment_correction = st.text_area(
                "Bone Alignment Correction details",
                height=80
            )

    with tab_outcome:
        st.markdown("<h4 style='color:#1e3a8a; margin-top:10px; margin-bottom:15px;'>Home Care & Outcomes</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            home_exercise = st.text_area(
                "Home Exercises Advised",
                height=80
            )
            posture_advice = st.text_area(
                "Posture & Lifestyle Advice",
                height=80
            )
        with col2:
            session_duration = st.number_input(
                "Session Duration (minutes)",
                min_value=1,
                max_value=240,
                value=30
            )
            session_date = st.date_input(
                "Session Date *"
            )
            session_outcome = st.selectbox(
                "Treatment Status / Session Outcome",
                [
                    "Improved",
                    "No Change",
                    "Mild Discomfort",
                    "Ongoing Care Required"
                ]
            )
            
            notes = st.text_area(
                "Therapist Remarks",
                height=60
            )

    st.markdown('</div>', unsafe_allow_html=True)

    submit = st.button(
        "Save Treatment Session"
    )

    if submit:
        if not consultation_id.strip():
            st.error("Consultation ID is required.")
            return
        if not therapy_type:
            st.warning("Please select at least one therapy type.")
            return

        treatment_data = {
            "consultation_id": consultation_id.strip(),
            "treatment_type": ", ".join(therapy_type),
            "treatment_plan": f"Adjustment Area: {chiropractic_adjustment_area}. Soft Tissue: {soft_tissue_therapy}. Nerve: {nerve_handling_technique}.",
            "medication": ayur_medicine.strip() if ayur_medicine.strip() else None,
            "session_number": 1,  # Default
            "session_date": str(session_date),
            "therapist_name": "Therapist",  # Default placeholder
            "treatment_status": session_outcome,
            "followup_required": True if session_outcome == "Ongoing Care Required" else False,
            "notes": f"Panchakarma: {panchakarma_type} using {oil_used}. Home Exercises: {home_exercise}. Remarks: {notes}."
        }

        try:
            payload = TreatmentService.register_treatment(treatment_data)
            with st.spinner("Logging treatment session..."):
                created_treatment = create_treatment(payload)

            if created_treatment:
                st.success("Treatment session logged successfully!")
                st.json(created_treatment[0])
            else:
                st.error("Failed to log treatment session.")
        except Exception as exc:
            st.error(f"{type(exc).__name__}: {exc}")
