import streamlit as st

from services.pain_assessment_crud import (
    create_assessment
)


def show_add_assessment_page():

    st.markdown('<h2 class="gradient-header">Add Pain Assessment</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Record a patient\'s physical symptoms, identify areas of pain, track pain severity, and log postural anomalies.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>👤 Patient & Pain Map</h4>", unsafe_allow_html=True)

        patient_id = st.text_input(
            "Patient ID (UUID)"
        )

        pain_areas = st.multiselect(
            "Select Pain Areas",
            [
                "Neck",
                "Shoulder",
                "Upper Back",
                "Lower Back",
                "Hip",
                "Knee",
                "Ankle"
            ]
        )

        st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True)
        pain_severity = st.slider(
            "Pain Severity Index (0 - 10)",
            0,
            10,
            5,
            help="0 is no pain, 10 is severe pain."
        )

    with col2:
        st.markdown("<h4 style='color:#0d9488; margin-top:0; border-bottom:2px solid #0d9488; padding-bottom:5px;'>🧍 Posture & Notes</h4>", unsafe_allow_html=True)

        posture = st.selectbox(
            "Observed Posture Deviation",
            [
                "Normal",
                "Forward Head",
                "Rounded Shoulders",
                "Kyphosis",
                "Lordosis"
            ]
        )

        notes = st.text_area(
            "Assessment Notes / Clinical Observations",
            height=125,
            placeholder="Describe pain triggers, joint mobility limits, gait variations..."
        )

    st.markdown('</div>', unsafe_allow_html=True)

    submit = st.button(
        "Save Assessment"
    )

    if submit:
        if not patient_id.strip():
            st.error("Patient ID is required.")
            return
        if not pain_areas:
            st.warning("Please select at least one pain area.")
            return

        assessment_data = {
            "patient_id": patient_id.strip(),
            "pain_areas": ", ".join(pain_areas),
            "pain_severity": pain_severity,
            "posture": posture,
            "notes": notes.strip()
        }

        with st.spinner("Saving assessment..."):
            created_assessment = create_assessment(assessment_data)

        if created_assessment:
            st.success("Pain assessment saved successfully!")
            st.json(created_assessment[0] if isinstance(created_assessment, list) else created_assessment)
        else:
            st.error("Failed to save assessment. Please check database connectivity.")