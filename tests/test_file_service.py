from services.file_service import FileService


class MockFile:

    def __init__(self, name):
        self.name = name

    def getvalue(self):
        return b"test"


def test_valid_file():

    file = MockFile("report.pdf")

    FileService.validate_file(file)

    assert True


def test_invalid_extension():

    file = MockFile("report.exe")

    try:
        FileService.validate_file(file)
        assert False

    except ValueError:
        assert True