import streamlit as st
import pandas as pd

from services.conversation_crud import get_all_conversations
from services.ai_crud import get_analysis_by_conversation


def _kpi_card(title, value, color="#0d9488"):
    st.markdown(
        f'<div style="background:white;padding:18px;border-radius:12px;border-left:5px solid {color};'
        f'box-shadow:0 2px 8px rgba(0,0,0,0.08);margin-bottom:10px;">'
        f'<p style="margin:0;color:#64748b;font-size:13px;font-weight:600;">{title}</p>'
        f'<p style="margin-top:8px;color:#1e293b;font-size:28px;font-weight:700;line-height:1;">{value}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )


def show_conversation_history_dashboard():

    st.markdown(
        '<h2 class="gradient-header">Conversation History Dashboard</h2>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p style="color:#64748b;margin-top:-10px;margin-bottom:20px;">'
        "Review all doctor-patient conversations, transcript previews, "
        "language statistics and recent activity."
        "</p>",
        unsafe_allow_html=True,
    )

    with st.spinner("Loading conversation history..."):
        conversations = get_all_conversations()

    if not conversations:
        st.info("No conversation history available.")
        return

    df = pd.DataFrame(conversations)

    total = len(df)

    audio_count = 0
    if "audio_file_url" in df.columns:
        audio_count = df["audio_file_url"].notna().sum()

    languages = 0
    if "language" in df.columns:
        languages = df["language"].nunique()

    transcript_count = 0
    if "raw_transcript" in df.columns:
        transcript_count = int(df["raw_transcript"].notna().sum())

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        _kpi_card("Total Conversations", total)
    with c2:
        _kpi_card("Audio Uploads", audio_count, "#3b82f6")
    with c3:
        _kpi_card("Languages", languages, "#8b5cf6")
    with c4:
        _kpi_card("With Transcripts", transcript_count, "#f59e0b")

    st.divider()

    search_query = st.text_input(
        "Search by Conversation ID, Consultation ID or Language",
        placeholder="Enter conversation ID, consultation ID or language...",
    )

    filtered = df.copy()

    if search_query:
        mask = pd.Series([False] * len(filtered), index=filtered.index)
        if "conversation_id" in filtered.columns:
            mask |= (
                filtered["conversation_id"]
                .astype(str)
                .str.lower()
                .str.contains(search_query.lower(), na=False)
            )
        if "consultation_id" in filtered.columns:
            mask |= (
                filtered["consultation_id"]
                .astype(str)
                .str.lower()
                .str.contains(search_query.lower(), na=False)
            )
        if "language" in filtered.columns:
            mask |= (
                filtered["language"]
                .astype(str)
                .str.lower()
                .str.contains(search_query.lower(), na=False)
            )
        filtered = filtered[mask]

    st.markdown(
        f'<p style="color:#64748b;font-size:14px;margin-bottom:8px;">'
        f'Showing <b>{len(filtered)}</b> conversation(s)</p>',
        unsafe_allow_html=True,
    )

    if filtered.empty:
        st.warning("No conversations match your search.")
        return

    for _, row in filtered.iterrows():

        conv_id = row.get("conversation_id", "N/A")
        consultation_id = row.get("consultation_id", "N/A")
        language = row.get("language", "N/A")
        source = row.get("source", "N/A")
        raw_created = row.get("created_at")
        created_at = str(raw_created).replace("T", " ")[:19] if raw_created else "N/A"
        audio_url = row.get("audio_file_url")
        transcript = row.get("raw_transcript")
        emotional_state = row.get("emotional_state")
        pain_keywords = row.get("pain_keywords")

        if transcript:
            status_icon = "🟢"
        elif audio_url:
            status_icon = "🟡"
        else:
            status_icon = "🔴"

        label = f"{status_icon}  Conversation — {str(conv_id)[:8]}...  |  Consultation: {str(consultation_id)[:8]}...  |  {language}"

        with st.expander(label):

            if transcript:
                st.success("Transcript Available")
            elif audio_url:
                st.warning("Audio Uploaded — Transcript Pending")
            else:
                st.error("Conversation Incomplete")

            meta_col, detail_col = st.columns([1, 1])

            with meta_col:
                st.markdown("**Conversation ID**")
                st.code(conv_id, language=None)
                st.markdown("**Consultation ID**")
                st.code(consultation_id, language=None)

            with detail_col:
                st.markdown("**Language**")
                st.write(language)
                st.markdown("**Source**")
                st.write(source)
                st.markdown("**Created At**")
                st.write(created_at)

            if audio_url:
                st.markdown("**Audio Recording**")
                st.markdown(
                    f'<a href="{audio_url}" target="_blank" style="'
                    f"color:#0d9488;font-weight:600;text-decoration:none;"
                    f'">▶ Play / Download Audio</a>',
                    unsafe_allow_html=True,
                )
                st.markdown("")

            if emotional_state or pain_keywords:
                badge_col1, badge_col2 = st.columns(2)
                with badge_col1:
                    if emotional_state:
                        st.markdown("**Emotional State**")
                        st.markdown(
                            f'<span style="background:#fef3c7;color:#92400e;padding:4px 10px;'
                            f'border-radius:20px;font-size:13px;">{emotional_state}</span>',
                            unsafe_allow_html=True,
                        )
                with badge_col2:
                    if pain_keywords:
                        st.markdown("**Pain Keywords**")
                        st.markdown(
                            f'<span style="background:#fee2e2;color:#991b1b;padding:4px 10px;'
                            f'border-radius:20px;font-size:13px;">{pain_keywords}</span>',
                            unsafe_allow_html=True,
                        )

            if transcript:
                st.markdown("**Transcript**")
                preview = transcript[:300] + ("..." if len(transcript) > 300 else "")
                st.markdown(
                    f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;'
                    f'padding:12px;font-size:14px;color:#334155;line-height:1.6;">{preview}</div>',
                    unsafe_allow_html=True,
                )
                if len(transcript) > 300:
                    with st.expander("Show full transcript"):
                        st.text(transcript)
            else:
                st.markdown(
                    '<p style="color:#94a3b8;font-size:13px;font-style:italic;">No transcript available.</p>',
                    unsafe_allow_html=True,
                )

            st.markdown("**AI Analysis**")
            ai_records = get_analysis_by_conversation(str(conv_id))
            if ai_records:
                ai = ai_records[0]
                risk = ai.get("risk_level") or "—"
                confidence = ai.get("ai_confidence")
                recovery = ai.get("recovery_prediction") or "—"
                summary = ai.get("summary")
                recommendations = ai.get("recommendations")
                symptoms = ai.get("extracted_symptoms")

                risk_colors = {
                    "high": ("#fee2e2", "#991b1b"),
                    "medium": ("#fef3c7", "#92400e"),
                    "low": ("#dcfce7", "#166534"),
                }
                risk_key = str(risk).lower()
                bg, fg = risk_colors.get(risk_key, ("#f1f5f9", "#334155"))

                ai_c1, ai_c2, ai_c3 = st.columns(3)
                with ai_c1:
                    st.markdown(
                        f'<div style="background:{bg};border-radius:10px;padding:14px;text-align:center;">'
                        f'<p style="margin:0;font-size:12px;color:#64748b;font-weight:600;">RISK LEVEL</p>'
                        f'<p style="margin:4px 0 0;font-size:22px;font-weight:700;color:{fg};">{risk.title()}</p>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                with ai_c2:
                    conf_display = f"{round(confidence * 100)}%" if isinstance(confidence, (int, float)) else "—"
                    st.markdown(
                        f'<div style="background:#eff6ff;border-radius:10px;padding:14px;text-align:center;">'
                        f'<p style="margin:0;font-size:12px;color:#64748b;font-weight:600;">CONFIDENCE</p>'
                        f'<p style="margin:4px 0 0;font-size:22px;font-weight:700;color:#1d4ed8;">{conf_display}</p>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                with ai_c3:
                    st.markdown(
                        f'<div style="background:#f0fdf4;border-radius:10px;padding:14px;text-align:center;">'
                        f'<p style="margin:0;font-size:12px;color:#64748b;font-weight:600;">RECOVERY</p>'
                        f'<p style="margin:4px 0 0;font-size:22px;font-weight:700;color:#166534;">{recovery}</p>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )

                st.markdown("")

                if summary:
                    st.markdown("**Summary**")
                    st.markdown(
                        f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;'
                        f'padding:12px;font-size:14px;color:#334155;line-height:1.6;">{summary[:400]}</div>',
                        unsafe_allow_html=True,
                    )

                if symptoms:
                    st.markdown("**Extracted Symptoms**")
                    st.markdown(
                        f'<span style="background:#fef3c7;color:#92400e;padding:4px 10px;'
                        f'border-radius:20px;font-size:13px;">{symptoms}</span>',
                        unsafe_allow_html=True,
                    )

                if recommendations:
                    st.markdown("**Recommendations**")
                    st.info(recommendations)

            else:
                st.markdown(
                    '<p style="color:#94a3b8;font-size:13px;font-style:italic;">No AI analysis linked to this conversation.</p>',
                    unsafe_allow_html=True,
                )
