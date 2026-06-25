import streamlit as st
from services.conversation_crud import create_conversation
from services.conversation_service import ConversationService
from services.audio_service import AudioService

def show_add_conversation_page():
    st.markdown('<h2 class="gradient-header">Capture Clinical Conversation</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#64748b; margin-top:-10px; margin-bottom: 20px;">Upload diagnostic audio files or log manual conversation transcripts between the doctor and patient.</p>', unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='color:#1e3a8a; margin-top:0; border-bottom:2px solid #3b82f6; padding-bottom:5px;'>🗣️ Recording Meta</h4>", unsafe_allow_html=True)
        
        consultation_id = st.text_input(
            "Consultation ID (UUID) *"
        )
        
        source = st.selectbox(
            "Recording Source *",
            ["Audio File Upload", "Manual Transcript Entry"]
        )
        
        uploaded_audio = None
        if source == "Audio File Upload":
            uploaded_audio = st.file_uploader(
                "Upload Patient Audio File (MP3, WAV, M4A) *",
                type=["mp3", "wav", "m4a"]
            )
            
        language = st.selectbox(
            "Transcript Language",
            ["English", "Hindi", "English & Hindi Mixed", "Other"]
        )

        emotional_state = st.selectbox(
            "Patient Emotional State",
            ["Calm", "Anxious", "Distressed", "Hopeful", "Fatigued"]
        )

    with col2:
        st.markdown("<h4 style='color:#0d9488; margin-top:0; border-bottom:2px solid #0d9488; padding-bottom:5px;'>📝 Transcript Notes</h4>", unsafe_allow_html=True)

        raw_transcript = st.text_area(
            "Raw Transcript Text *",
            height=120,
            placeholder="e.g. \nDoctor: Where does it hurt?\nPatient: In my lower back, it shoots down my left leg."
        )

        speaker_separation = st.text_area(
            "Speaker Separation Notes",
            height=80,
            placeholder="e.g. Speaker 0 is Doctor, Speaker 1 is Patient"
        )
        
        additional_notes = st.text_area(
            "Additional Notes",
            height=60
        )

    st.markdown('</div>', unsafe_allow_html=True)

    submit = st.button(
        "Save Conversation Logs"
    )

    if submit:
        if not consultation_id.strip():
            st.error("Consultation ID is required.")
            return
        if not raw_transcript.strip():
            st.error("Raw Transcript is required.")
            return
        if source == "Audio File Upload" and uploaded_audio is None:
            st.warning("Please upload the audio file first.")
            return

        conversation_data = {
            "consultation_id": consultation_id.strip(),
            "source": source,
            "raw_transcript": raw_transcript.strip(),
            "language": language,
            "speaker_separation": speaker_separation.strip() if speaker_separation.strip() else None,
            "emotional_state": emotional_state,
            "pain_keywords": None,  # Detect keywords in later AI phase
            "additional_notes": additional_notes.strip() if additional_notes.strip() else None
        }

        audio_file_url = None
        try:
            # Handle audio upload if present
            if source == "Audio File Upload" and uploaded_audio is not None:
                with st.spinner("Uploading audio recording to Supabase Storage..."):
                    audio_file_url = AudioService.upload_audio(
                        consultation_id=consultation_id.strip(),
                        uploaded_file=uploaded_audio
                    )
                conversation_data["audio_file_url"] = audio_file_url

            # Register local validation
            payload = ConversationService.register_conversation(conversation_data)
            
            with st.spinner("Saving conversation details..."):
                created_conversation = create_conversation(payload)

            if created_conversation:
                st.success("Conversation logs captured successfully!")
                st.json(created_conversation[0])
                if audio_file_url:
                    st.info(f"Audio file saved successfully! URL: {audio_file_url}")
            else:
                st.error("Failed to save conversation logs.")
        except Exception as exc:
            st.error(f"{type(exc).__name__}: {exc}")
