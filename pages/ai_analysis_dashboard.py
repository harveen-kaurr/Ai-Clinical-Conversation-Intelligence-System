import streamlit as st
import pandas as pd

from services.ai_crud import get_all_analysis


def _kpi_card(title, value, color="#0d9488"):
    st.markdown(
        f'<div style="background:white;padding:18px;border-radius:12px;border-left:5px solid {color};'
        f'box-shadow:0 2px 8px rgba(0,0,0,0.08);margin-bottom:10px;">'
        f'<p style="margin:0;color:#64748b;font-size:13px;font-weight:600;">{title}</p>'
        f'<p style="margin-top:8px;color:#1e293b;font-size:28px;font-weight:700;line-height:1;">{value}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )



def show_ai_analysis_dashboard():

    st.markdown(
        '<h2 class="gradient-header">AI Analysis Dashboard</h2>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p style="color:#64748b;margin-top:-10px;margin-bottom:20px;">'
        "Review AI generated summaries, recommendations, confidence scores, "
        "recovery predictions and clinical risk levels."
        "</p>",
        unsafe_allow_html=True,
    )

    with st.spinner("Loading AI analyses..."):
        analyses = get_all_analysis()

    if not analyses:
        st.warning("No AI analysis records found.")
        return

    df = pd.DataFrame(analyses)

    total = len(df)

    avg_confidence = 0.0
    if "ai_confidence" in df.columns:
        raw_avg = df["ai_confidence"].fillna(0).mean()
        avg_confidence = round(raw_avg * 100, 1) if raw_avg <= 1 else round(raw_avg, 1)

    risk_col = df["risk_level"].astype(str).str.lower() if "risk_level" in df.columns else pd.Series()
    high   = int((risk_col == "high").sum())
    medium = int((risk_col == "medium").sum())
    low    = int((risk_col == "low").sum())

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        _kpi_card("Total Analyses", total)
    with c2:
        _kpi_card("Avg Confidence", f"{avg_confidence}%", "#3b82f6")
    with c3:
        _kpi_card("High Risk", high, "#ef4444")
    with c4:
        _kpi_card("Medium Risk", medium, "#f59e0b")
    with c5:
        _kpi_card("Low Risk", low, "#22c55e")

    st.divider()

    search = st.text_input(
        "Search Analysis",
        placeholder="Analysis ID / Conversation ID / Risk Level...",
    )

    filtered = df.copy()

    if search:
        filtered = filtered[
            filtered.astype(str)
            .apply(lambda row: row.str.contains(search, case=False, na=False))
            .any(axis=1)
        ]

    st.markdown(
        f'<p style="color:#64748b;font-size:14px;margin-bottom:8px;">'
        f'Showing <b>{len(filtered)}</b> analysis record(s)</p>',
        unsafe_allow_html=True,
    )

    if filtered.empty:
        st.warning("No records match your search.")
        return

    for _, row in filtered.iterrows():

        analysis_id   = row.get("analysis_id", "N/A")
        conv_id       = row.get("conversation_id", "N/A")
        risk          = row.get("risk_level") or "Unknown"
        confidence    = row.get("ai_confidence")
        surgery       = row.get("surgery_probability")
        recovery      = row.get("recovery_prediction")
        emotional     = row.get("emotional_state")
        summary       = row.get("summary")
        recommendations = row.get("recommendations")
        symptoms      = row.get("extracted_symptoms")
        pain_keywords = row.get("pain_keywords")
        raw_created   = row.get("created_at")
        created_at    = str(raw_created).replace("T", " ")[:19] if raw_created else "N/A"

        risk_icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}
        icon = risk_icons.get(str(risk).lower(), "⚪")

        conf_display = f"{round(confidence * 100)}%" if isinstance(confidence, (int, float)) else "—"
        label = (
            f"{icon}  Analysis: {str(analysis_id)[:8]}...  |  "
            f"Conversation: {str(conv_id)[:8]}...  |  "
            f"Risk: {str(risk).title()}  |  Confidence: {conf_display}"
        )

        with st.expander(label):

            ai_c1, ai_c2, ai_c3 = st.columns(3)

            with ai_c1:
                risk_colors = {
                    "high":   ("#fee2e2", "#991b1b"),
                    "medium": ("#fef3c7", "#92400e"),
                    "low":    ("#dcfce7", "#166534"),
                }
                bg, fg = risk_colors.get(str(risk).lower(), ("#f1f5f9", "#334155"))
                st.markdown(
                    f'<div style="background:{bg};border-radius:10px;padding:14px;text-align:center;">'
                    f'<p style="margin:0;font-size:12px;color:#64748b;font-weight:600;">RISK LEVEL</p>'
                    f'<p style="margin:4px 0 0;font-size:22px;font-weight:700;color:{fg};">{str(risk).title()}</p>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

            with ai_c2:
                st.markdown(
                    f'<div style="background:#eff6ff;border-radius:10px;padding:14px;text-align:center;">'
                    f'<p style="margin:0;font-size:12px;color:#64748b;font-weight:600;">CONFIDENCE</p>'
                    f'<p style="margin:4px 0 0;font-size:22px;font-weight:700;color:#1d4ed8;">{conf_display}</p>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

            with ai_c3:
                surgery_display = f"{round(surgery * 100)}%" if isinstance(surgery, (int, float)) else "—"
                st.markdown(
                    f'<div style="background:#fdf4ff;border-radius:10px;padding:14px;text-align:center;">'
                    f'<p style="margin:0;font-size:12px;color:#64748b;font-weight:600;">SURGERY PROB.</p>'
                    f'<p style="margin:4px 0 0;font-size:22px;font-weight:700;color:#7e22ce;">{surgery_display}</p>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

            st.markdown("")

            meta_c1, meta_c2 = st.columns(2)
            with meta_c1:
                st.markdown("**Analysis ID**")
                st.code(analysis_id, language=None)
                st.markdown("**Conversation ID**")
                st.code(conv_id, language=None)
            with meta_c2:
                st.markdown("**Created At**")
                st.write(created_at)
                if recovery:
                    st.markdown("**Recovery Prediction**")
                    st.success(recovery)
                if emotional:
                    st.markdown("**Emotional State**")
                    st.info(emotional)

            if symptoms or pain_keywords:
                badge_c1, badge_c2 = st.columns(2)
                with badge_c1:
                    if symptoms:
                        st.markdown("**Extracted Symptoms**")
                        st.markdown(
                            f'<span style="background:#fef3c7;color:#92400e;padding:4px 10px;'
                            f'border-radius:20px;font-size:13px;">{symptoms}</span>',
                            unsafe_allow_html=True,
                        )
                with badge_c2:
                    if pain_keywords:
                        st.markdown("**Pain Keywords**")
                        st.markdown(
                            f'<span style="background:#fee2e2;color:#991b1b;padding:4px 10px;'
                            f'border-radius:20px;font-size:13px;">{pain_keywords}</span>',
                            unsafe_allow_html=True,
                        )

            if summary:
                st.markdown("**AI Summary**")
                st.markdown(
                    f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;'
                    f'padding:14px;font-size:14px;color:#334155;line-height:1.7;">{summary}</div>',
                    unsafe_allow_html=True,
                )
                st.download_button(
                    "Download Summary",
                    summary,
                    file_name=f"analysis_{analysis_id}.txt",
                    key=f"dl_{analysis_id}",
                )

            if recommendations:
                st.markdown("**Recommendations**")
                st.info(recommendations)

    st.divider()

    st.subheader("Risk Distribution")

    if "risk_level" in filtered.columns:
        risk_counts = (
            filtered["risk_level"]
            .astype(str)
            .str.title()
            .value_counts()
        )
        st.bar_chart(risk_counts)
