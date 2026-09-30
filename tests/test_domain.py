from anything2pdf.domain.formats import is_supported_extension
from anything2pdf.domain.jobs import JobState

def test_supported_extensions():
    # File hợp lệ
    assert is_supported_extension(".docx") is True
    assert is_supported_extension(".PDF") is False  # File PDF không phải là input hợp lệ
    
    # Kiểm tra tính không phân biệt hoa thường
    assert is_supported_extension(".DOCX") is True
    assert is_supported_extension(".pPtX") is True
    # File rác hoặc chưa hỗ trợ
    assert is_supported_extension(".txt") is False
    assert is_supported_extension(".exe") is False
def test_job_states():
    # Kiểm tra Enum có các thuộc tính mong đợi
    assert JobState.PENDING.name == "PENDING"
    assert JobState.SUCCEEDED.name == "SUCCEEDED"