from services.audio_service import (
    AudioService
)


class MockUploadedFile:

    def __init__(
        self,
        file_name,
        file_content
    ):

        self.name = file_name

        self._content = (
            file_content
        )

    def getvalue(self):

        return (
            self._content
        )


def main():

    print("\n")
    print("=" * 60)
    print("AUDIO SERVICE DEMO")
    print("=" * 60)

    try:

        uploaded_audio = (
            MockUploadedFile(
                "patient_audio.mp3",
                b"Sample Audio Content"
            )
        )

        AudioService.validate_audio(
            uploaded_audio
        )

        print(
            "\n✅ Audio validation completed successfully."
        )

        print("\nAudio Information")
        print("-" * 60)

        print(
            f"File Name : {uploaded_audio.name}"
        )

        print(
            f"File Size : {len(uploaded_audio.getvalue())} bytes"
        )

        print(
            "\n✔ Audio is ready for upload."
        )

    except Exception as e:

        print(
            f"\n❌ Error : {e}"
        )

    print("\n")
    print("=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)


if __name__ == "__main__":

    main()