import streamlit as st

from services.pain_assessment_crud import (
    get_assessment_by_id,
    update_assessment
)


def show_edit_assessment_page():

    st.markdown('<h2 class="gradient-header">Edit Pain Assessment</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Load an existing pain assessment record by ID, modify observations, and commit the changes.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    load_col1, load_col2 = st.columns([3, 1])
    with load_col1:
        assessment_id = st.text_input(
            "Enter Assessment ID (UUID)"
        )
    with load_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        load_btn = st.button("Load Assessment")
    st.markdown('</div>', unsafe_allow_html=True)

    if load_btn:
        with st.spinner("Loading assessment log..."):
            assessment = get_assessment_by_id(
                assessment_id
            )

        if assessment:
            st.session_state["assessment"] = assessment[0]
            st.session_state["assessment_id"] = assessment_id
        else:
            st.error("Assessment not found. Please verify the ID.")

    if "assessment" in st.session_state:
        assessment = st.session_state["assessment"]

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>✏️ Update Assessment Details</h4>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            pain_areas = st.text_input(
                "Pain Areas (comma separated)",
                value=assessment.get("pain_areas", "")
            )

            pain_severity = st.slider(
                "Pain Severity Index (0 - 10)",
                0,
                10,
                int(assessment.get("pain_severity", 0))
            )

        with col2:
            posture = st.text_input(
                "Observed Posture Deviation",
                value=assessment.get("posture", "")
            )

            notes = st.text_area(
                "Clinical Notes",
                value=assessment.get("notes", "") or "",
                height=100
            )

        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Update Assessment"):
            updated_data = {
                "pain_areas": pain_areas,
                "pain_severity": pain_severity,
                "posture": posture,
                "notes": notes
            }

            with st.spinner("Updating assessment record..."):
                result = update_assessment(
                    st.session_state["assessment_id"],
                    updated_data
                )

            if result:
                st.success("Assessment updated successfully!")
                del st.session_state["assessment"]
                del st.session_state["assessment_id"]
            else:
                st.error("Failed to update assessment.")