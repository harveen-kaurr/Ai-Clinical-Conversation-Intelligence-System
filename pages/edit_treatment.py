import streamlit as st
import datetime
from services.treatment_crud import (
    get_treatment_by_id,
    update_treatment
)

def show_edit_treatment_page():
    st.markdown('<h2 class="gradient-header">Edit Treatment Session</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Load an existing treatment session by UUID, modify the session details, and save the changes to the database.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    load_col1, load_col2 = st.columns([3, 1])
    with load_col1:
        treatment_id = st.text_input(
            "Enter Treatment UUID",
            placeholder="e.g. 12345678-1234-1234-1234-123456789012"
        )
    with load_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        load_btn = st.button("Load Treatment")
    st.markdown('</div>', unsafe_allow_html=True)

    if load_btn:
        if not treatment_id.strip():
            st.error("Please enter a valid Treatment UUID.")
            return

        with st.spinner("Loading treatment details..."):
            treatment = get_treatment_by_id(treatment_id.strip())

        if treatment:
            st.session_state["edit_treatment"] = treatment
            st.session_state["edit_treatment_id"] = treatment_id.strip()
            st.success("Treatment session loaded successfully!")
        else:
            st.error("Treatment session not found. Please verify the UUID.")

    if "edit_treatment" in st.session_state:
        treatment = st.session_state["edit_treatment"]
        edit_id = st.session_state["edit_treatment_id"]

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>✏️ Modify Treatment Details (ID: {edit_id})</h4>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            consultation_id = st.text_input(
                "Consultation ID (UUID) *",
                value=treatment.get("consultation_id", ""),
                disabled=True,
                help="The consultation ID is fixed for this treatment session."
            )
            
            therapy_options = [
                "Chiropractic Adjustment",
                "Soft Tissue Therapy",
                "Osteopathy handling",
                "Ayurveda & Panchakarma",
                "Spine Decompression",
                "Nerve flossing",
                "Bone Alignment"
            ]
            
            db_therapies_str = treatment.get("treatment_type", "")
            db_therapies = [t.strip() for t in db_therapies_str.split(", ") if t.strip()]
            
            # Ensure all parsed options are available in multiselect list
            for item in db_therapies:
                if item not in therapy_options:
                    therapy_options.append(item)
                    
            therapy_type = st.multiselect(
                "Therapy Type *",
                options=therapy_options,
                default=db_therapies
            )

            treatment_plan = st.text_area(
                "Treatment Plan / Procedure Details",
                value=treatment.get("treatment_plan", "") or "",
                height=100
            )

            medication = st.text_area(
                "Prescribed Medicine / Oils",
                value=treatment.get("medication", "") or "",
                height=100
            )

        with col2:
            session_number = st.number_input(
                "Session Number",
                min_value=1,
                max_value=100,
                value=int(treatment.get("session_number", 1))
            )
            
            session_date_val = datetime.date.today()
            if treatment.get("session_date"):
                try:
                    session_date_val = datetime.date.fromisoformat(str(treatment.get("session_date")))
                except Exception:
                    pass
            
            session_date = st.date_input(
                "Session Date *",
                value=session_date_val
            )

            therapist_name = st.text_input(
                "Therapist Name",
                value=treatment.get("therapist_name", "Therapist") or ""
            )

            status_options = [
                "Improved",
                "No Change",
                "Mild Discomfort",
                "Ongoing Care Required"
            ]
            db_status = treatment.get("treatment_status", "Improved")
            try:
                status_idx = status_options.index(db_status)
            except ValueError:
                status_options.append(db_status)
                status_idx = len(status_options) - 1

            treatment_status = st.selectbox(
                "Treatment Status / Session Outcome",
                options=status_options,
                index=status_idx
            )

            followup_required = st.checkbox(
                "Follow-up Required",
                value=bool(treatment.get("followup_required", False))
            )

        st.markdown("<hr style='margin: 15px 0; border:0; border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)
        
        notes = st.text_area(
            "Therapist Remarks / Home Exercises / Notes",
            value=treatment.get("notes", "") or "",
            height=100
        )

        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Update Treatment Session"):
            if not therapy_type:
                st.error("Please select at least one therapy type.")
                return

            updated_data = {
                "treatment_type": ", ".join(therapy_type),
                "treatment_plan": treatment_plan.strip(),
                "medication": medication.strip() if medication.strip() else None,
                "session_number": session_number,
                "session_date": str(session_date),
                "therapist_name": therapist_name.strip() if therapist_name.strip() else "Therapist",
                "treatment_status": treatment_status,
                "followup_required": followup_required,
                "notes": notes.strip() if notes.strip() else None
            }

            with st.spinner("Updating treatment session..."):
                try:
                    result = update_treatment(edit_id, updated_data)
                    if result:
                        st.success("Treatment session updated successfully!")
                        # Clean session state so page reloads clean
                        del st.session_state["edit_treatment"]
                        del st.session_state["edit_treatment_id"]
                    else:
                        st.error("Failed to update treatment session in database.")
                except Exception as exc:
                    st.error(f"Error updating treatment: {exc}")
