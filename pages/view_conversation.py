import streamlit as st
import pandas as pd
from services.conversation_crud import get_all_conversations

def show_view_conversation_page():
    st.markdown('<h2 class="gradient-header">View Conversation History</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">List of all patient-doctor clinical conversation recordings and transcripts available in the system.</p>', unsafe_allow_html=True)

    with st.spinner("Loading conversation logs..."):
        conversations = get_all_conversations()

    if not conversations:
        st.info("No clinical conversations found in the database.")
        return

    df = pd.DataFrame(conversations)

    total_logs = len(df)
    audio_logs_count = len(df[df['source'].astype(str).str.lower() == 'audio file upload']) if 'source' in df.columns else 0
    languages_count = df['language'].nunique() if 'language' in df.columns else 0

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total Conversations Captured", f"{total_logs}")
    with m2:
        st.metric("Audio Recording Logs", f"{audio_logs_count}")
    with m3:
        st.metric("Languages Used", f"{languages_count}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:0; color:#1e3a8a;">📋 Conversation Registry</h4>', unsafe_allow_html=True)
    st.dataframe(
        df,
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
