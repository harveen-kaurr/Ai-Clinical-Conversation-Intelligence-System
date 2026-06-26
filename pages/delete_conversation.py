import streamlit as st
from services.conversation_crud import (
    get_conversation_by_id,
    delete_conversation
)

def show_delete_conversation_page():
    st.markdown('<h2 class="gradient-header" style="color: #dc2626;">Delete Conversation Log</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Permanently remove a logged clinical conversation record from the database.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    load_col1, load_col2 = st.columns([3, 1])
    with load_col1:
        conversation_id = st.text_input(
            "Enter Conversation UUID",
            placeholder="e.g. 12345678-1234-1234-1234-123456789012"
        )
    with load_col2:
        st.markdown("<div style='height:28px;'></div>", unsafe_allow_html=True)
        load_btn = st.button("Load Conversation")
    st.markdown('</div>', unsafe_allow_html=True)

    if load_btn:
        if not conversation_id.strip():
            st.error("Please enter a valid Conversation UUID.")
            return

        with st.spinner("Retrieving conversation details..."):
            conversation = get_conversation_by_id(conversation_id.strip())

        if conversation:
            st.session_state["delete_conversation"] = conversation
            st.session_state["delete_conversation_id"] = conversation_id.strip()
            st.success("Conversation details loaded successfully!")
        else:
            st.error("Conversation record not found. Please verify the UUID.")

    if "delete_conversation" in st.session_state:
        conversation = st.session_state["delete_conversation"]
        del_id = st.session_state["delete_conversation_id"]

        st.markdown('<div class="custom-card" style="border-left: 5px solid #dc2626;">', unsafe_allow_html=True)
        st.markdown("<h4 style='color:#dc2626; margin-top:0;'>⚠️ Confirm Conversation Deletion</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="margin-bottom: 20px; font-size: 0.95rem; line-height: 1.6;">
            <strong>Recording Source:</strong> {conversation.get('source')}<br/>
            <strong>Language:</strong> {conversation.get('language')}<br/>
            <strong>Patient Emotional State:</strong> {conversation.get('emotional_state') or 'N/A'}<br/>
            <strong>Consultation ID:</strong> <code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.8rem;">{conversation.get('consultation_id')}</code><br/>
            <strong>Conversation UUID:</strong> <code style="background:#f1f5f9; padding: 2px 4px; border-radius:4px; font-size:0.8rem;">{del_id}</code>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background: #f8fafc; border-radius: 6px; padding: 15px; margin-bottom: 20px; font-size: 0.9rem; border-left: 3px solid #dc2626; white-space: pre-wrap; font-family: monospace;">
            <strong>Raw Transcript Text:</strong><br/><br/>{conversation.get('raw_transcript')}
        </div>
        """, unsafe_allow_html=True)

        if conversation.get('audio_file_url'):
            st.info("Note: This conversation has an associated audio recording saved in Supabase storage.")

        st.error("🚨 WARNING: This action is irreversible. The dialogue transcripts and associated database records will be permanently deleted.")

        confirm = st.checkbox("I understand and confirm I want to delete this conversation log.")
        
        if confirm:
            if st.button("Delete Conversation"):
                with st.spinner("Deleting conversation from database..."):
                    try:
                        result = delete_conversation(del_id)
                        if result:
                            st.success("Conversation record deleted successfully.")
                            del st.session_state["delete_conversation"]
                            del st.session_state["delete_conversation_id"]
                        else:
                            st.error("Delete operation failed. Please check database permissions.")
                    except Exception as exc:
                        st.error(f"Error deleting conversation: {exc}")
        st.markdown('</div>', unsafe_allow_html=True)
