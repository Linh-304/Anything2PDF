"""
Định nghĩa các định dạng file được hỗ trợ trong phiên bản MVP.
Hỗ trợ Word, Powerpoint và Excel
"""

SUPPORTED_WORD_FORMATS = {".doc", ".docx", ".odt"}
SUPPORTED_POWERPOINT_FORMATS = {".ppt", ".pptx", ".odp"}
SUPPORTED_EXCEL_FORMATS = {".xls", ".xlsx", ".ods"}

ALL_SUPPORTED_EXTENSIONS = (
    SUPPORTED_WORD_FORMATS
    | SUPPORTED_POWERPOINT_FORMATS
    | SUPPORTED_EXCEL_FORMATS
)

def is_supported_extension(extension: str) -> bool:
    """
    Kiểm tra xem một đuôi file có được hỗ trợ hay không.
    """

    return extension.lower() in ALL_SUPPORTED_EXTENSIONS