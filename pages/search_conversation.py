import streamlit as st
import pandas as pd
from services.conversation_crud import search_conversations

def show_search_conversation_page():
    st.markdown('<h2 class="gradient-header">Search Conversation Transcripts</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Lookup patient encounter dialogue logs by entering a Consultation ID or filtering by Language.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>🔍 Search Parameters</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        consultation_id = st.text_input(
            "Filter by Consultation ID (UUID)",
            placeholder="e.g. 12345678-1234-1234-1234-123456789012"
        )
    with col2:
        language = st.text_input(
            "Filter by Language",
            placeholder="e.g. English, Hindi"
        )
    st.markdown('</div>', unsafe_allow_html=True)

    search = st.button(
        "Search Conversations"
    )

    if search:
        if not consultation_id.strip() and not language.strip():
            st.warning("Please provide at least one search filter.")
            return

        with st.spinner("Searching records..."):
            results = search_conversations(
                consultation_id=consultation_id.strip() if consultation_id.strip() else None,
                language=language.strip() if language.strip() else None
            )

        if not results:
            st.error("No matching conversations found.")
            return

        st.success(f"Found {len(results)} matching conversation logs.")

        for idx, item in enumerate(results):
            source = item.get('source')
            st.markdown(f"""
            <div style="background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
                <div style="border-bottom: 1px solid #f1f5f9; padding-bottom: 10px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0; color: #1e3a8a; font-weight: 700;">🗣️ Conversation Transcript #{idx+1}</h4>
                    <span style="font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 100px; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd;">{source}</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; font-size: 0.9rem; margin-bottom: 15px;">
                    <div><span style="color:#64748b; font-weight:500;">Language:</span><br/><strong>{item.get('language')}</strong></div>
                    <div><span style="color:#64748b; font-weight:500;">Emotional State:</span><br/>{item.get('emotional_state') or 'N/A'}</div>
                    <div><span style="color:#64748b; font-weight:500;">Consultation ID:</span><br/><code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.75rem;">{item.get('consultation_id')}</code></div>
                    <div><span style="color:#64748b; font-weight:500;">Conversation UUID:</span><br/><code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.75rem;">{item.get('conversation_id')}</code></div>
                </div>
                
                <div style="background: #f8fafc; border-radius: 6px; padding: 15px; margin-bottom: 15px; font-size: 0.9rem; border-left: 3px solid #3b82f6; white-space: pre-wrap; font-family: monospace;">
                    <strong>Raw Transcript Text:</strong><br/><br/>{item.get('raw_transcript')}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Optional Audio Player if URL exists
            audio_url = item.get('audio_file_url')
            if audio_url:
                st.audio(audio_url)
