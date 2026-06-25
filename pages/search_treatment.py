import streamlit as st
import pandas as pd
from services.treatment_crud import search_treatments

def show_search_treatment_page():
    st.markdown('<h2 class="gradient-header">Search Treatment Logs</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Lookup treatment history logs by entering a Consultation ID or Therapy Type filter.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>🔍 Search Parameters</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        consultation_id = st.text_input(
            "Filter by Consultation ID (UUID)",
            placeholder="e.g. 12345678-1234-1234-1234-123456789012"
        )
    with col2:
        treatment_type = st.text_input(
            "Filter by Therapy / Treatment Type",
            placeholder="e.g. Chiropractic, Panchakarma"
        )
    st.markdown('</div>', unsafe_allow_html=True)

    search = st.button(
        "Search Treatments"
    )

    if search:
        if not consultation_id.strip() and not treatment_type.strip():
            st.warning("Please provide at least one search filter.")
            return

        with st.spinner("Searching records..."):
            results = search_treatments(
                consultation_id=consultation_id.strip() if consultation_id.strip() else None,
                treatment_type=treatment_type.strip() if treatment_type.strip() else None
            )

        if not results:
            st.error("No matching treatment records found.")
            return

        st.success(f"Found {len(results)} matching treatment log(s).")

        for idx, item in enumerate(results):
            status = item.get('treatment_status')
            if status == "Improved":
                badge_style = "background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0;"
            elif status == "Mild Discomfort":
                badge_style = "background: #fee2e2; color: #b91c1c; border: 1px solid #fecaca;"
            else:
                badge_style = "background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd;"

            st.markdown(f"""
            <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
                <div style="border-bottom: 1px solid #f1f5f9; padding-bottom: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0; color: #1e3a8a; font-weight: 700;">🧘 Session #{idx+1}</h4>
                    <span style="font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 100px; {badge_style}">{status}</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; font-size: 0.9rem; margin-bottom: 10px;">
                    <div><span style="color:#64748b; font-weight:500;">Therapy Type:</span><br/><span style="color:#0d9488; font-weight:600;">{item.get('treatment_type')}</span></div>
                    <div><span style="color:#64748b; font-weight:500;">Session Date:</span><br/>{item.get('session_date')}</div>
                    <div><span style="color:#64748b; font-weight:500;">Consultation ID:</span><br/><code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.75rem;">{item.get('consultation_id')}</code></div>
                    <div><span style="color:#64748b; font-weight:500;">Treatment UUID:</span><br/><code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.75rem;">{item.get('treatment_id')}</code></div>
                </div>
                <div style="margin-top: 10px; padding-top: 10px; border-top: 1px dashed #f1f5f9; font-size:0.85rem; color:#475569;">
                    <strong>Plan details:</strong> {item.get('treatment_plan') or 'N/A'}<br/>
                    <strong>Prescriptions / Remarks:</strong> {item.get('notes') or 'N/A'}
                </div>
            </div>
            """, unsafe_allow_html=True)
