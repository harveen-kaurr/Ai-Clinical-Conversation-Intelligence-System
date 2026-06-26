import streamlit as st
from services.conversation_crud import (
    get_conversation_by_id,
    update_conversation
)
from services.audio_service import AudioService

def show_edit_conversation_page():
    st.markdown('<h2 class="gradient-header">Edit Conversation Log</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Load an existing conversation encounter log, update transcript dialogues or audio recordings, and save the updates.</p>', unsafe_allow_html=True)

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

        with st.spinner("Loading conversation details..."):
            conversation = get_conversation_by_id(conversation_id.strip())

        if conversation:
            st.session_state["edit_conversation"] = conversation
            st.session_state["edit_conversation_id"] = conversation_id.strip()
            st.success("Conversation log loaded successfully!")
        else:
            st.error("Conversation log not found. Please verify the UUID.")

    if "edit_conversation" in st.session_state:
        conversation = st.session_state["edit_conversation"]
        edit_id = st.session_state["edit_conversation_id"]

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>✏️ Modify Conversation Details (ID: {edit_id})</h4>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            consultation_id = st.text_input(
                "Consultation ID (UUID) *",
                value=conversation.get("consultation_id", ""),
                disabled=True,
                help="The consultation ID is fixed for this conversation log."
            )
            
            source_options = ["Audio File Upload", "Manual Transcript Entry"]
            db_source = conversation.get("source", "Manual Transcript Entry")
            source_idx = source_options.index(db_source) if db_source in source_options else 0
            
            source = st.selectbox(
                "Recording Source *",
                options=source_options,
                index=source_idx
            )
            
            # Display current audio file url and replacement input
            current_audio_url = conversation.get("audio_file_url", "")
            uploaded_audio = None
            if source == "Audio File Upload":
                if current_audio_url:
                    st.markdown(f"**Current Audio File:** [Play / Download]({current_audio_url})")
                    st.audio(current_audio_url)
                
                uploaded_audio = st.file_uploader(
                    "Replace / Upload Patient Audio File (MP3, WAV, M4A)",
                    type=["mp3", "wav", "m4a"]
                )
            
            lang_options = ["English", "Hindi", "English & Hindi Mixed", "Other"]
            db_lang = conversation.get("language", "English")
            if db_lang not in lang_options:
                lang_options.append(db_lang)
            lang_idx = lang_options.index(db_lang)
            
            language = st.selectbox(
                "Transcript Language",
                options=lang_options,
                index=lang_idx
            )

            emo_options = ["Calm", "Anxious", "Distressed", "Hopeful", "Fatigued"]
            db_emo = conversation.get("emotional_state", "Calm")
            if db_emo not in emo_options:
                emo_options.append(db_emo)
            emo_idx = emo_options.index(db_emo)

            emotional_state = st.selectbox(
                "Patient Emotional State",
                options=emo_options,
                index=emo_idx
            )

        with col2:
            st.markdown("<h5 style='color:#0d9488; margin-top:0;'>📝 Dialogue & Notes</h5>", unsafe_allow_html=True)
            
            raw_transcript = st.text_area(
                "Raw Transcript Text *",
                value=conversation.get("raw_transcript", "") or "",
                height=150
            )

            speaker_separation = st.text_area(
                "Speaker Separation Notes",
                value=conversation.get("speaker_separation", "") or "",
                height=80
            )
            
            additional_notes = st.text_area(
                "Additional Notes",
                value=conversation.get("additional_notes", "") or "",
                height=80
            )

        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Update Conversation Logs"):
            if not raw_transcript.strip():
                st.error("Raw Transcript is required.")
                return

            updated_data = {
                "source": source,
                "raw_transcript": raw_transcript.strip(),
                "language": language,
                "speaker_separation": speaker_separation.strip() if speaker_separation.strip() else None,
                "emotional_state": emotional_state,
                "additional_notes": additional_notes.strip() if additional_notes.strip() else None
            }

            audio_file_url = current_audio_url
            try:
                # Handle audio replacement
                if source == "Audio File Upload" and uploaded_audio is not None:
                    with st.spinner("Uploading new audio recording to Supabase Storage..."):
                        audio_file_url = AudioService.upload_audio(
                            consultation_id=conversation.get("consultation_id"),
                            uploaded_file=uploaded_audio
                        )
                elif source == "Manual Transcript Entry":
                    audio_file_url = None # Remove if source changed to manual

                updated_data["audio_file_url"] = audio_file_url

                with st.spinner("Updating conversation logs..."):
                    result = update_conversation(edit_id, updated_data)
                    if result:
                        st.success("Conversation logs updated successfully!")
                        del st.session_state["edit_conversation"]
                        del st.session_state["edit_conversation_id"]
                    else:
                        st.error("Failed to update conversation in database.")
            except Exception as exc:
                st.error(f"Error updating conversation: {exc}")
