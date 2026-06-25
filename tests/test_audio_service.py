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

        self._file_content = (
            file_content
        )

    def getvalue(self):

        return (
            self._file_content
        )


def print_result(
    title,
    success,
    message
):

    print("\n" + "=" * 55)

    print(title)

    print("=" * 55)

    if success:

        print(
            f"✅ PASS : {message}"
        )

    else:

        print(
            f"❌ FAIL : {message}"
        )


def test_valid_audio():

    try:

        audio = (
            MockUploadedFile(
                "sample.mp3",
                b"Dummy Audio Content"
            )
        )

        AudioService.validate_audio(
            audio
        )

        print_result(
            "VALID AUDIO TEST",
            True,
            "Audio validation successful."
        )

    except Exception as e:

        print_result(
            "VALID AUDIO TEST",
            False,
            str(e)
        )


def test_invalid_extension():

    try:

        audio = (
            MockUploadedFile(
                "sample.pdf",
                b"Dummy Content"
            )
        )

        AudioService.validate_audio(
            audio
        )

        print_result(
            "INVALID FILE TYPE TEST",
            False,
            "Validation should have failed."
        )

    except Exception as e:

        print_result(
            "INVALID FILE TYPE TEST",
            True,
            str(e)
        )


def test_large_audio():

    try:

        large_audio = (
            MockUploadedFile(
                "large.mp3",
                b"x" * (
                    51 * 1024 * 1024
                )
            )
        )

        AudioService.validate_audio(
            large_audio
        )

        print_result(
            "FILE SIZE TEST",
            False,
            "Validation should have failed."
        )

    except Exception as e:

        print_result(
            "FILE SIZE TEST",
            True,
            str(e)
        )


if __name__ == "__main__":

    print("\n")

    print("=" * 55)
    print("AUDIO SERVICE TEST REPORT")
    print("=" * 55)

    test_valid_audio()

    test_invalid_extension()

    test_large_audio()

    print("\n")

    print("=" * 55)
    print("ALL TESTS COMPLETED")
    print("=" * 55)