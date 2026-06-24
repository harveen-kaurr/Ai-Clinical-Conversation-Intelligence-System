from services.file_service import FileService


class MockFile:

    def __init__(self):
        self.name = "test_report.txt"
        self.type = "text/plain"

    def getvalue(self):
        return b"This is a test MRI report"


consultation_id = "4776398a-3629-49bd-a47a-51dfda616e52"

result = FileService.upload_file(
    consultation_id=consultation_id,
    uploaded_file=MockFile(),
    file_type="MRI"
)

print(result)