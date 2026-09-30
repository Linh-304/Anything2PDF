# Anything2PDF

Ứng dụng desktop offline chuyển đổi tài liệu văn phòng (Word, Excel, PowerPoint) sang PDF sử dụng LibreOffice headless.

## Yêu cầu hệ thống

- Hệ điều hành: Windows
- Python: 3.12+
- Yêu cầu bên ngoài: LibreOffice (người dùng tự cài trên Windows)

## Môi trường phát triển

1. Tạo môi trường: `python -m venv .venv`
2. Kích hoạt: `.\.venv\Scripts\activate`
3. Cài đặt (Editable mode): `pip install -e ".[dev]"`

## Chạy ứng dụng & Test

- Chạy UI: `anything2pdf`
- Chạy Test: `pytest`

## Các chính sách (Policies) được chốt ở Phase 0

- **Concurrency (Xử lý đồng thời):** Mặc định là 1 (tránh treo máy).
- **Quét thư mục:** Không đệ quy (chỉ lấy file trực tiếp bên trong).
- **Timeout:** 5 phút cho mỗi quá trình gọi process.
