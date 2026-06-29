import os
import tempfile

import requests
import whisper


class WhisperService:

    def __init__(self):

        self.model = whisper.load_model("base")

    def transcribe_audio(
        self,
        audio_url: str
    ) -> str:

        response = requests.get(audio_url)

        response.raise_for_status()

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_audio:

            temp_audio.write(
                response.content
            )

            temp_audio_path = (
                temp_audio.name
            )

        result = self.model.transcribe(
            temp_audio_path
        )

        os.remove(
            temp_audio_path
        )

        transcript = (
            result.get(
                "text",
                ""
            ).strip()
        )

        return transcript