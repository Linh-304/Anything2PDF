from enum import Enum, auto
from dataclasses import dataclass
from pathlib import Path
from uuid import UUID

class JobState(Enum):
    """Các trạng thái vòng đời của một conversion job theo project plan."""
    PENDING = auto()
    RUNNING = auto()
    SUCCEEDED = auto()
    FAILED = auto()
    CANCELED = auto()

class ErrorCategory(Enum):
    """Phân loại các lỗi tối thiểu theo MVP."""
    INPUT_NOT_FOUND = "Không tìm thấy file gốc"
    UNSUPPORTED_EXTENSION = "Định dạng không được hỗ trợ"
    READ_ERROR = "Không thể đọc file"
    ENGINE_NOT_FOUND = "Không tìm thấy công cụ chuyển đổi (LibreOffice)"
    ENGINE_CRASHED = "Công cụ chuyển đổi bị lỗi khi chạy"
    TIMEOUT = "Quá thời gian xử lý"
    CANCELLED = "Đã bị hủy bỏ"
    OUTPUT_ERROR = "Không thể tạo file PDF"
    UNKNOWN = "Lỗi không xác định"

@dataclass
class ConversionError:
    """Model chứa thông tin lỗi để có thể hiển thị an toàn trên UI."""
    category: ErrorCategory
    message: str

@dataclass
class ConversionJob:
    """Cấu trúc dữ liệu đại diện cho một tác vụ chuyển đổi file."""
    id: UUID
    input_path: Path
    output_dir: Path
    output_path: Path | None = None
    state: JobState = JobState.PENDING
    progress: int = 0
    error: ConnectionError | None = None