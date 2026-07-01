import streamlit as st
import json

from services.ai_crud import (
    get_analysis_by_id,
    get_analysis_by_conversation
)


def show_search_ai_analysis_page():

    st.markdown('<h2 class="gradient-header">Search AI Analysis</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#64748b; margin-top:-10px; margin-bottom:20px;">'
        'Lookup AI-generated clinical reports by Analysis ID or Conversation ID.</p>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    search_col1, search_col2 = st.columns([1, 2])
    with search_col1:
        search_type = st.selectbox(
            "Search Parameter",
            ["Analysis ID", "Conversation ID"]
        )
    with search_col2:
        search_value = st.text_input(
            "Enter Search Term",
            placeholder=f"Enter {search_type.lower()}..."
        )
    st.markdown('</div>', unsafe_allow_html=True)

    if not st.button("Search Database"):
        return

    if not search_value.strip():
        st.warning("Please enter a search query.")
        return

    with st.spinner("Searching records..."):
        if search_type == "Analysis ID":
            result = get_analysis_by_id(search_value.strip())
            results = [result] if result else []
        else:
            results = get_analysis_by_conversation(search_value.strip()) or []

    if not results:
        st.error("No matching AI analysis record found.")
        return

    results.sort(key=lambda x: x.get("created_at") or "", reverse=True)

    st.success(f"Found {len(results)} matching analysis record(s).")

    for i, analysis in enumerate(results):
        _render_analysis_card(analysis, index=i + 1, total=len(results))


def _render_analysis_card(analysis: dict, index: int = 1, total: int = 1):

    structured = analysis.get("structured_output") or {}
    if isinstance(structured, str):
        try:
            structured = json.loads(structured)
        except json.JSONDecodeError:
            structured = {}

    rules = structured.get("clinical_rules", {}) if isinstance(structured, dict) else {}
    prediction = structured.get("prediction_engine", {}) if isinstance(structured, dict) else {}

    risk = analysis.get("risk_level", "N/A")
    risk_color = {"High": "#dc2626", "Medium": "#d97706", "Low": "#16a34a"}.get(risk, "#64748b")

    st.markdown(f"""
    <div style="background:white; border:1px solid #e2e8f0; border-radius:10px; padding:20px; margin-bottom:15px; box-shadow:0 4px 6px -1px rgb(0 0 0 / 0.05);">
        <div style="border-bottom:1px solid #f1f5f9; padding-bottom:10px; margin-bottom:15px; display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; color:#1e3a8a; font-weight:700; font-size:1.1rem;">Record {index} of {total}</h3>
            <span style="background:{'#dcfce7; color:#16a34a' if index == 1 else '#e0f2fe; color:#0369a1'}; font-size:0.75rem; font-weight:700; padding:4px 8px; border-radius:100px;">{'Latest' if index == 1 else 'Analysis Record'}</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:15px; font-size:0.9rem;">
            <div><span style="color:#64748b; font-weight:500;">Analysis ID:</span><br/><code style="background:#f1f5f9; color:#0f172a; padding:2px 6px; border-radius:4px; font-size:0.78rem;">{analysis.get('analysis_id', 'N/A')}</code></div>
            <div><span style="color:#64748b; font-weight:500;">Conversation ID:</span><br/><code style="background:#f1f5f9; color:#0f172a; padding:2px 6px; border-radius:4px; font-size:0.78rem;">{analysis.get('conversation_id', 'N/A')}</code></div>
            <div><span style="color:#64748b; font-weight:500;">Risk Level:</span><br/><span style="color:{risk_color}; font-weight:700;">{risk}</span></div>
            <div><span style="color:#64748b; font-weight:500;">Surgery Probability:</span><br/><span style="font-weight:600;">{analysis.get('surgery_probability', 'N/A')}</span></div>
            <div><span style="color:#64748b; font-weight:500;">AI Confidence:</span><br/><span style="font-weight:600;">{analysis.get('ai_confidence', 'N/A')}</span></div>
            <div><span style="color:#64748b; font-weight:500;">Emotional State:</span><br/>{analysis.get('emotional_state', 'N/A')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Clinical Summary")
    st.write(analysis.get("summary", "N/A"))

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Extracted Symptoms")
        st.write(analysis.get("extracted_symptoms", "N/A"))
    with col2:
        st.subheader("Pain Keywords")
        st.write(analysis.get("pain_keywords", "N/A"))

    st.metric("Recovery Prediction", analysis.get("recovery_prediction", "N/A"))

    st.subheader("Recommendations")
    st.info(analysis.get("recommendations", "N/A"))

    st.divider()
    st.subheader("Clinical Rules")

    c1, c2 = st.columns(2)
    with c1:
        st.write(f"**Follow-up:** {rules.get('follow_up', 'N/A')}")
        st.write(f"**Risk (Rule Engine):** {rules.get('rule_risk_level', 'N/A')}")
        st.write(f"**Surgery Probability:** {rules.get('rule_surgery_probability', 'N/A')}")
        st.write(f"**Recovery Prediction:** {rules.get('rule_recovery_prediction', 'N/A')}")
    with c2:
        st.write("**Suggested Tests**")
        for item in rules.get("suggested_tests", []):
            st.success(item)

    st.subheader("Recommended Therapy")
    therapy = rules.get("recommended_therapy", [])
    if therapy:
        cols = st.columns(2)
        for i, item in enumerate(therapy):
            with cols[i % 2]:
                st.info(item)

    st.subheader("Clinical Flags")
    flags = rules.get("flags", [])
    if flags:
        cols = st.columns(3)
        for i, item in enumerate(flags):
            with cols[i % 3]:
                st.warning(item)

    st.divider()
    st.subheader("Prediction Engine")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Pain Level", prediction.get("pain_level", "N/A"))
        st.metric("Patient Category", prediction.get("patient_category", "N/A"))
    with col2:
        st.metric("Therapy Priority", prediction.get("therapy_priority", "N/A"))
        st.metric("Recovery Priority", prediction.get("recovery_priority", "N/A"))

    with st.expander("View Complete AI JSON"):
        st.json(analysis)
