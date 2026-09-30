# Anything2PDF - Project Plan

> Tài liệu nguồn duy nhất mô tả bối cảnh, mục tiêu, phạm vi, kiến trúc, tiêu chuẩn kỹ thuật và quy trình phát triển của dự án Anything2PDF. Mọi thay đổi lớn về sản phẩm hoặc kiến trúc phải được đối chiếu với tài liệu này và cập nhật tại đây trước khi triển khai.

- **Tên dự án:** Anything2PDF
- **Loại sản phẩm:** Ứng dụng desktop chuyển đổi tài liệu sang PDF
- **Trạng thái:** Greenfield project, đang ở giai đoạn chuẩn bị triển khai
- **Phiên bản mục tiêu đầu tiên:** MVP / 0.x
- **Nền tảng MVP:** Windows
- **Ngôn ngữ giao diện MVP:** Tiếng Việt
- **Mô hình xử lý:** Offline, xử lý trực tiếp trên máy người dùng

## 0. Working agreement và vai trò hướng dẫn

Đây là dự án người dùng tự phát triển. Trợ lý đóng vai trò mentor kỹ thuật, người giải thích, reviewer và người đồng hành trong quá trình học và triển khai; trợ lý không phải người tự động thực hiện toàn bộ codebase.

### 0.1 Quyền sở hữu và giới hạn can thiệp

- Người dùng là người trực tiếp viết, tạo, sửa và xóa code của dự án.
- Trợ lý **chỉ được phép can thiệp vào file `project-plan.md`** trong workspace Anything2PDF.
- Trợ lý không được tự ý tạo, sửa, xóa hoặc đổi tên bất kỳ file nào khác, bao gồm source code, test, cấu hình, README, script build và tài liệu khác.
- Trợ lý không được tự ý commit, tạo branch, reset hoặc revert thay đổi của người dùng.
- Khi cần thay đổi `project-plan.md`, trợ lý phải trình bày phần muốn sửa, nội dung dự kiến và lý do; chỉ được sửa sau khi người dùng đồng ý rõ ràng.
- Nếu một yêu cầu có vẻ cần chỉnh file ngoài `project-plan.md`, trợ lý phải dừng ở mức hướng dẫn hoặc đề xuất để người dùng tự thực hiện.

### 0.2 Quy trình làm việc theo task

Mỗi task phát triển được xử lý theo chu trình sau:

1. **Context:** xác định mục tiêu task, vị trí kiến thức liên quan và các ràng buộc từ plan.
2. **Explain:** giải thích khái niệm, API, thiết kế hoặc lỗi cần xử lý ở mức phù hợp với bước hiện tại.
3. **Plan:** chia task thành bước nhỏ, chỉ rõ file mà người dùng sẽ tự chỉnh và tiêu chí hoàn thành.
4. **Your implementation:** người dùng tự viết code trong workspace.
5. **Review:** người dùng gửi code, lỗi hoặc kết quả kiểm tra; trợ lý phân tích và đề xuất sửa, không tự sửa file ngoài `project-plan.md`.
6. **Verification:** xác định command/test/manual check để người dùng tự chạy; diễn giải kết quả và lỗi nếu có.
7. **Plan update:** nếu có thay đổi về scope, kiến trúc hoặc quyết định kỹ thuật, trợ lý đề xuất cập nhật plan và xin phép trước.
8. **Version Control:** Cuối mỗi Phase, người dùng sẽ commit và push code lên GitHub. Trợ lý sẽ hướng dẫn và cung cấp commit message tương ứng.

Trợ lý không tự chuyển sang task kế tiếp nếu task hiện tại còn lỗi quan trọng hoặc người dùng chưa hiểu phần nền tảng cần thiết. Khi có nhiều lựa chọn, trợ lý phải giải thích trade-off và đưa ra khuyến nghị, nhưng quyết định cuối cùng thuộc về người dùng.

### 0.3 Cách hướng dẫn ưu tiên

- Ưu tiên giải thích ngắn, cụ thể, có ví dụ nhỏ và gắn với code của task hiện tại.
- Ưu tiên thư viện, pattern và cấu trúc đã được chốt trong tài liệu này.
- Không đưa ra một khối code lớn mà không giải thích trách nhiệm của từng phần.
- Khuyến khích người dùng tự viết phiên bản đầu tiên; trợ lý tập trung vào câu hỏi gợi mở, review và chẩn đoán.
- Khi đề xuất thay đổi kiến trúc, phải nêu ảnh hưởng tới scope, test, hiệu năng, packaging và phase hiện tại.

---

## 1. Tổng quan dự án

Anything2PDF là một ứng dụng desktop có giao diện đồ họa, giúp người dùng chuyển các file tài liệu văn phòng sang PDF bằng thao tác kéo-thả đơn giản.

Người dùng có thể kéo một hoặc nhiều file từ Windows Explorer vào ứng dụng, hoặc chọn file/thư mục thông qua hộp thoại. Ứng dụng đưa các file vào danh sách chờ, kiểm tra tính hợp lệ, chuyển đổi theo batch và hiển thị trạng thái của từng file.

Mục tiêu của sản phẩm không phải là thay thế toàn bộ Microsoft Office. Mục tiêu là cung cấp một công cụ tiện ích, dễ dùng, offline, có workflow rõ ràng và đủ ổn định cho các tác vụ chuyển đổi tài liệu thông thường.

### 1.1 Vấn đề cần giải quyết

Các thao tác chuyển nhiều tài liệu sang PDF thường có những bất tiện sau:

- Người dùng phải mở từng file bằng ứng dụng văn phòng.
- Quy trình lặp lại nhiều lần khi có nhiều tài liệu.
- Khó theo dõi file nào đã chuyển đổi thành công hoặc thất bại.
- Việc xử lý file output trùng tên có thể dẫn tới ghi đè dữ liệu.
- Người dùng cần một công cụ đơn giản, không yêu cầu upload tài liệu lên dịch vụ cloud.

Anything2PDF giải quyết các vấn đề này bằng một hàng đợi chuyển đổi trực quan, xử lý batch, trạng thái rõ ràng và chính sách không ghi đè mặc định.

### 1.2 Tầm nhìn

Tạo một công cụ chuyển đổi tài liệu có trải nghiệm đơn giản như một tiện ích hệ thống nhưng được xây dựng với nền tảng đủ tốt để mở rộng thêm engine, định dạng, nền tảng và workflow tự động trong các phiên bản sau.

### 1.3 Nguyên tắc sản phẩm

1. **Đơn giản trước:** người dùng có thể hoàn thành tác vụ chính mà không cần đọc tài liệu dài.
2. **Offline by default:** nội dung tài liệu không rời khỏi máy người dùng.
3. **Không phá dữ liệu:** mặc định không ghi đè file output đã tồn tại.
4. **UI không bị treo:** chuyển đổi luôn chạy ngoài UI thread.
5. **Lỗi phải hành động được:** thông báo lỗi cần cho người dùng biết nguyên nhân và bước xử lý tiếp theo.
6. **Engine có thể thay thế:** code ứng dụng không phụ thuộc trực tiếp vào một implementation duy nhất.
7. **Phạm vi có kiểm soát:** chỉ mở rộng sau khi MVP đạt checkpoint và có test tương ứng.

---

## 2. Mục tiêu và tiêu chí thành công

### 2.1 Mục tiêu MVP

MVP phải cho phép người dùng Windows:

- Khởi động ứng dụng desktop.
- Kéo-thả nhiều file được hỗ trợ vào cửa sổ.
- Chọn file hoặc thư mục bằng dialog.
- Chọn thư mục lưu PDF.
- Chuyển đổi nhiều file theo batch.
- Theo dõi trạng thái từng file và tiến độ tổng thể.
- Retry file bị lỗi.
- Hủy job đang chạy.
- Nhận biết khi LibreOffice chưa được cài đặt hoặc không thể chạy.
- Nhận kết quả mà không làm mất hoặc ghi đè file đã tồn tại.

### 2.2 Tiêu chí thành công cấp sản phẩm

MVP được xem là đạt khi:

- Người dùng mới có thể hiểu workflow chính mà không cần hướng dẫn trực tiếp.
- DOCX, PPTX và XLSX mẫu được chuyển đổi thành PDF hợp lệ trên Windows.
- Batch có thể tiếp tục xử lý các file còn lại khi một file thất bại.
- UI vẫn phản hồi trong quá trình chuyển đổi.
- Cancel không để lại process LibreOffice mồ côi hoặc file PDF dở dang.
- Ứng dụng không gửi file hoặc telemetry ra ngoài máy.
- Bản build PyInstaller chạy được trên máy Windows không có môi trường phát triển.
- Các giới hạn về font và layout được ghi rõ, không tạo kỳ vọng fidelity tuyệt đối.

### 2.3 Definition of Done cho một task

Một task chỉ được xem là hoàn thành khi:

- Người dùng đã tự cập nhật code hoặc tài liệu liên quan theo task.
- Người dùng hiểu trách nhiệm của phần code vừa viết và có thể giải thích luồng xử lý chính.
- Có test phù hợp với mức độ rủi ro của thay đổi, hoặc có lý do rõ ràng nếu chưa thể test tự động.
- Người dùng đã chạy verification được thống nhất và ghi nhận kết quả.
- Không tạo lỗi lint/type/test mới trong phạm vi liên quan.
- Không phá vỡ các contract đã được định nghĩa trong tài liệu này.
- Đã kiểm tra trên Windows nếu task liên quan đến subprocess, file system, drag-and-drop hoặc packaging.
- Có ghi chú về giới hạn hoặc quyết định mới nếu hành vi sản phẩm thay đổi.
- Nếu cần cập nhật `project-plan.md`, thay đổi đã được đề xuất và người dùng đã đồng ý trước khi cập nhật.

---

## 3. Phạm vi sản phẩm

### 3.1 Định dạng đầu vào trong MVP

| Nhóm | Định dạng |
|---|---|
| Word / văn bản | `.doc`, `.docx`, `.odt` |
| PowerPoint / trình chiếu | `.ppt`, `.pptx`, `.odp` |
| Excel / bảng tính | `.xls`, `.xlsx`, `.ods` |

Danh sách extension phải được quản lý tập trung trong domain hoặc configuration, không rải rác trong UI.

### 3.2 Chức năng trong MVP

#### Thêm file

- Kéo-thả một hoặc nhiều file.
- Chọn nhiều file bằng file dialog.
- Chọn thư mục để quét các file có extension được hỗ trợ.
- Bỏ qua file không được hỗ trợ với lý do rõ ràng.
- Tránh thêm cùng một input path nhiều lần trong cùng một batch.

#### Quản lý job

- Mỗi file đầu vào tương ứng với một `ConversionJob`.
- Hiển thị tên file, loại file, trạng thái, progress và thông báo lỗi ngắn.
- Có thể remove job chưa chạy.
- Có thể retry job thất bại.
- Có thể cancel job đang chạy hoặc hủy phần còn chờ.
- Có thể xóa các job đã hoàn thành khỏi danh sách.

#### Output

- Người dùng chọn thư mục output.
- Tên PDF mặc định lấy từ stem của input.
- Nếu tên đã tồn tại, tạo tên không trùng theo quy tắc deterministic, ví dụ `document (1).pdf`, `document (2).pdf`.
- Không ghi đè output mặc định.
- Chỉ coi job là thành công khi file PDF cuối cùng tồn tại và có kích thước hợp lệ.

#### Trạng thái và lỗi

Các trạng thái cơ bản:

- `PENDING`: đã thêm và đang chờ.
- `RUNNING`: đang được engine xử lý.
- `SUCCEEDED`: đã tạo PDF thành công.
- `FAILED`: kết thúc với lỗi có thể hiển thị.
- `CANCELLED`: bị người dùng hoặc hệ thống hủy.

Các nhóm lỗi tối thiểu:

- Input không tồn tại.
- Extension không được hỗ trợ.
- Không đọc được input.
- Không tìm thấy LibreOffice.
- LibreOffice không khởi động được.
- Process timeout.
- Process bị hủy.
- Không có quyền ghi output.
- Output không được tạo hoặc không hợp lệ.
- Lỗi không xác định có thông tin chẩn đoán kèm theo.

### 3.3 Ngoài phạm vi MVP

Các nội dung sau không được tự động đưa vào MVP:

- macOS hoặc Linux.
- Watch folder.
- CLI độc lập.
- OCR.
- Chỉnh sửa nội dung PDF.
- Merge, split hoặc reorder PDF.
- Chuyển đổi qua cloud.
- Telemetry hoặc analytics.
- Đóng gói LibreOffice cùng ứng dụng.
- Cam kết PDF giống Microsoft Office tuyệt đối.
- Các tùy chọn PDF nâng cao như password, watermark, PDF/A hoặc nén tùy chỉnh.
- Hệ thống plugin công khai.

---

## 4. Quyết định sản phẩm đã chốt

| Chủ đề | Quyết định | Lý do |
|---|---|---|
| Nền tảng | Windows trước | Tập trung vào workflow kéo-thả và giảm chi phí kiểm thử ban đầu |
| Python | Python 3.12 | Ổn định và tương thích tốt với hệ sinh thái dự kiến |
| GUI | PySide6 + Qt Widgets thuần | Hỗ trợ desktop native, drag-and-drop, model/view và signals/slots mà không cần UI framework bổ sung |
| Engine MVP | LibreOffice headless | Miễn phí, offline, hỗ trợ nhiều định dạng văn phòng |
| Engine boundary | Có abstraction/interface | Cho phép bổ sung engine khác mà không viết lại application layer |
| LibreOffice | Người dùng cài riêng | Giảm kích thước và độ phức tạp của bản MVP |
| Fidelity | Giữ layout tốt ở mức thực dụng | Phù hợp LibreOffice nhưng không hứa tương đương tuyệt đối với Office |
| UI language | Tiếng Việt | Phù hợp người dùng mục tiêu hiện tại |
| Output collision | Tự tạo tên không trùng | Không ghi đè và không làm gián đoạn batch bằng dialog liên tục |
| Network | Không có network call | Bảo vệ dữ liệu và giữ workflow offline |
| Logging | Tối thiểu | Hỗ trợ chẩn đoán nhưng không ghi nội dung tài liệu |
| Packaging | PyInstaller onedir | Đủ cho MVP và dễ debug hơn one-file |
| Concurrency | Bounded worker queue, mặc định 1 job | Ưu tiên máy yếu; chỉ tăng concurrency sau khi đo CPU/RAM và có cấu hình rõ ràng |
| UI framework bổ sung | Không dùng trong MVP | Giảm dependency, kích thước build và rủi ro styling/DPI |
| Runtime download | Không tự động tải Python package khi chạy | PyInstaller bundle sẵn runtime; dependency phải được kiểm soát từ build |
| LibreOffice download | Không tự động tải trong MVP | Ứng dụng chỉ phát hiện và hướng dẫn người dùng cài LibreOffice riêng |
| Web runtime | Không dùng QtWebEngine/WebView | Tránh tăng memory footprint và kích thước ứng dụng |

Các quyết định trên chỉ được thay đổi khi có một lý do kỹ thuật hoặc sản phẩm rõ ràng, kèm đánh giá ảnh hưởng tới scope và test.

---

## 5. Tech stack

### 5.1 Runtime và ngôn ngữ

- Python 3.12.
- Windows là môi trường target đầu tiên.
- Code phải ưu tiên standard library khi không cần dependency bên ngoài.
- Dùng type hints cho public function, model và boundary giữa các layer.
- Không tải hoặc cài Python dependency trong lúc ứng dụng đang chạy.
- Bản phát hành phải bundle Python runtime và production dependencies bằng PyInstaller.

### 5.2 GUI

- PySide6, chỉ sử dụng các module Qt cần thiết như `QtCore`, `QtGui` và `QtWidgets`.
- Qt Widgets thuần, không dùng QtWebEngine, WebView hoặc frontend web nhúng.
- Qt signals/slots cho giao tiếp giữa worker và presentation.
- `QTableView` kết hợp `QAbstractTableModel` hoặc model tương đương cho danh sách job; không tạo một widget nặng riêng cho từng file.
- Drag-and-drop events của Qt.
- Qt Style Sheet (QSS) nhỏ, có tổ chức để tạo visual identity; ưu tiên style native và spacing rõ ràng trước khi thêm theme package.
- Icon và resource phải được kiểm soát license và đóng gói cùng artifact khi cần.

UI không được gọi trực tiếp subprocess conversion trong event handler. UI chỉ tạo command/use case, nhận event và render state.

Không dùng các thư viện UI bổ sung như QFluentWidgets, CustomTkinter, ttkbootstrap, DearPyGui hoặc Flet trong MVP. `qt-material` chỉ là lựa chọn thử nghiệm sau khi UI chức năng hoàn thiện và phải vượt qua benchmark trước khi được giữ lại.

### 5.3 Conversion engine

- LibreOffice CLI, thường thông qua executable `soffice` hoặc binary tương ứng trên Windows.
- Chạy bằng `subprocess`.
- Sử dụng `--headless` và profile tạm riêng cho mỗi job hoặc nhóm job phù hợp.
- Capture exit code, stdout và stderr.
- Có timeout.
- Có cơ chế cancel process tree phù hợp Windows.

Lệnh cụ thể phải được đóng gói trong infrastructure adapter, không xuất hiện trong widget hoặc domain.

### 5.4 Standard library dự kiến

- `pathlib`: xử lý path.
- `subprocess`: gọi LibreOffice.
- `tempfile`: profile và output tạm.
- `dataclasses`: model dữ liệu.
- `enum`: trạng thái và error categories.
- `queue` hoặc `concurrent.futures`: worker orchestration.
- `threading` hoặc Qt worker pattern: chạy tác vụ ngoài UI thread.
- `logging`: log tối thiểu.
- `shutil` và `os`: file system/process utilities khi cần.

### 5.5 Testing và quality

- `pytest` cho unit và integration tests.
- `pytest-qt` nếu phù hợp cho UI smoke tests.
- Ruff cho lint và format.
- Pyright/Pylance cho type checking nếu được bật trong môi trường phát triển.
- Test fixture office thật phải được kiểm soát nguồn, kích thước và mục đích sử dụng.
- Integration tests phụ thuộc LibreOffice phải có marker; unit tests vẫn chạy được khi máy developer chưa cài LibreOffice.

### 5.6 Production dependencies

Production dependency Python chính của MVP là:

- `PySide6`.

LibreOffice là external runtime, không phải Python package và không được cài bằng `pip`.

Không thêm `pandas`, `numpy`, `Pillow`, `pypdf`, `PyMuPDF`, `requests`, `aiohttp`, `psutil`, `watchdog` hoặc `qasync` vào MVP nếu chưa có use case và benchmark cụ thể.

### 5.7 Development dependencies

Development dependencies dự kiến:

- `pytest`.
- `pytest-qt`.
- `ruff`.
- `pyright` nếu cần type check độc lập với Pylance.
- `pyinstaller`.

Các package này không phải runtime requirement của người dùng cuối và không được đưa vào production dependency nếu PyInstaller không cần chúng.

### 5.8 Dependency và license policy

- Lock hoặc pin version dependency trong cấu hình build để artifact có thể tái tạo.
- Kiểm tra license của PySide6, Qt runtime, icon, font, theme và dependency transitive trước release.
- Khi phân phối PySide6/Qt, kèm notices và thực hiện các nghĩa vụ phù hợp với license LGPL/GPL của thành phần được sử dụng.
- Không thêm package chỉ vì có giao diện đẹp nếu package đó làm tăng đáng kể kích thước, memory hoặc rủi ro license.
- Mọi dependency mới phải nêu rõ mục đích, kích thước/ảnh hưởng runtime, license, phương án thay thế và test cần bổ sung.

### 5.9 Packaging

- PyInstaller.
- Bản MVP là onedir.
- LibreOffice không được bundle trong MVP.
- Python runtime và production dependencies được bundle trong artifact; người dùng không cần cài Python hoặc chạy `pip install`.
- Ứng dụng không tự động tải LibreOffice trong lúc chạy. Khi thiếu LibreOffice, ứng dụng hiển thị hướng dẫn cài đặt rõ ràng.
- Build phải có script hoặc command tái tạo được.
- Artifact cần có version rõ ràng.

---

## 6. Kiến trúc hệ thống

### 6.1 Nguyên tắc phân lớp

```text
Presentation (PySide6 UI)
        |
        v
Application (use cases, orchestration, events)
        |
        v
Domain (jobs, states, validation, policies)
        |
        v
Infrastructure (LibreOffice, subprocess, filesystem, logging)
```

Dependency đi từ ngoài vào trong. Domain không được import PySide6, `subprocess` hoặc chi tiết LibreOffice.

### 6.2 Domain layer

Domain layer chứa quy tắc nghiệp vụ thuần, có thể test mà không cần GUI hoặc LibreOffice.

Thành phần dự kiến:

- `ConversionJob`: input path, output directory, output path dự kiến, state, progress, error, timestamps.
- `JobState`: enum trạng thái.
- `ConversionError`: mã lỗi và message an toàn cho UI.
- `SupportedFormats`: registry extension và nhóm định dạng.
- `InputValidator`: kiểm tra path, extension và khả năng đọc.
- `OutputNamingPolicy`: sinh tên output không trùng.
- `JobStatePolicy`: kiểm soát transition hợp lệ.

Domain phải đảm bảo:

- Không transition ngược tùy tiện.
- Không đánh dấu `SUCCEEDED` nếu chưa xác nhận output.
- Không ghi đè file theo policy mặc định.
- Không chứa logic hiển thị widget.

### 6.3 Application layer

Application layer điều phối workflow nhưng không biết chi tiết UI.

Thành phần dự kiến:

- `AddFilesUseCase`.
- `ValidateInputsUseCase`.
- `ConvertBatchUseCase`.
- `RetryJobUseCase`.
- `CancelJobUseCase`.
- `ConversionQueue`.
- `JobEvent` hoặc event protocol.
- `ConversionEngine` protocol/interface.

Event có thể chứa:

- Job id.
- Event type.
- State mới.
- Progress.
- Output path.
- Error category và message.
- Batch summary.

Application layer phải độc lập với cách event được render. UI có thể adapter event này vào Qt signals.

### 6.4 Infrastructure layer

Infrastructure hiện thực các boundary phụ thuộc môi trường.

Thành phần dự kiến:

- `LibreOfficeLocator`: tìm executable tại các vị trí Windows phổ biến hoặc từ configuration.
- `LibreOfficeEngine`: xây dựng command, chạy subprocess và kiểm tra output.
- `ProcessRunner`: wrapper để test subprocess và timeout.
- `TemporaryProfileManager`: tạo và cleanup profile riêng.
- `OutputFileManager`: output tạm, atomic finalize và collision handling.
- `ProcessTermination`: hủy process tree trên Windows.
- `AppLogger`: log tối thiểu, không ghi nội dung file.

### 6.5 Presentation layer

Màn hình chính cần có:

- Tiêu đề ứng dụng.
- Drop zone nổi bật.
- Nút thêm file.
- Nút thêm thư mục.
- Bộ chọn thư mục output.
- Danh sách các job.
- Tiến độ từng job và tổng thể.
- Nút chuyển đổi.
- Nút retry.
- Nút cancel.
- Nút remove hoặc clear completed.
- Khu vực hiển thị summary và lỗi.
- Hành động mở thư mục output sau khi hoàn thành.

UI phải có trạng thái rõ ràng cho:

- Chưa có job.
- Đang chờ input.
- Đang convert.
- Có job thành công một phần.
- Tất cả thành công.
- Có lỗi.
- Thiếu LibreOffice.
- Đang hủy.

### 6.5.1 Nguyên tắc hiệu năng UI

- Không dùng QtWebEngine, WebView hoặc frontend web nhúng.
- Không render preview tài liệu trong MVP.
- Dùng `QTableView`/model cho danh sách job thay vì tạo một widget nặng riêng cho mỗi file.
- Hạn chế animation; chỉ dùng hover state, progress và chuyển trạng thái cần thiết.
- Không nạp toàn bộ nội dung tài liệu vào memory để hiển thị danh sách.
- Cập nhật UI theo event có kiểm soát, tránh phát hàng nghìn repaint liên tục cho một job.
- Danh sách lớn phải vẫn có thể cuộn và thao tác được khi conversion đang chạy.

### 6.6 Luồng chuyển đổi chuẩn

```text
User drops/selects files
        |
        v
Collect paths and remove duplicates
        |
        v
Validate supported extension and readable input
        |
        v
Create ConversionJob in PENDING
        |
        v
Resolve output directory and non-colliding output path
        |
        v
Queue job
        |
        v
Worker starts LibreOffice with isolated temporary profile
        |
        v
Capture process result and validate generated PDF
        |
        +--> Success: finalize output and mark SUCCEEDED
        |
        +--> Failure: cleanup and mark FAILED
        |
        +--> Cancel: terminate process, cleanup, mark CANCELLED
        |
        v
Publish event to UI and update batch summary
```

### 6.7 Isolation và dữ liệu tạm

- Mỗi job phải có không gian tạm có thể xác định và cleanup.
- Không chỉnh sửa input gốc.
- Output chỉ được công bố sau khi conversion hoàn tất và validation pass.
- Không đưa nội dung tài liệu vào log.
- Nếu cleanup thất bại, log path và lỗi kỹ thuật nhưng không làm lộ nội dung tài liệu.

### 6.8 Queue và tài nguyên máy

- Concurrency mặc định là `1` để ưu tiên máy yếu và tránh mở nhiều LibreOffice process.
- Chỉ cho phép tăng concurrency sau khi có benchmark CPU, RAM, thời gian hoàn thành và độ ổn định.
- Queue phải giới hạn số worker; không tạo một thread/process cho mỗi input không giới hạn.
- Job pending không được mở LibreOffice trước khi worker nhận job.
- Hủy batch phải giải phóng job pending và dừng process của job running theo policy.
- UI phải hiển thị trạng thái đang xử lý nhưng không cần hiển thị số liệu hệ thống liên tục trong MVP.

---

## 7. Thiết kế UX và workflow

### 7.1 Workflow chính

1. Người dùng mở Anything2PDF.
2. Ứng dụng kiểm tra LibreOffice.
3. Người dùng kéo-thả file hoặc bấm chọn file/thư mục.
4. Ứng dụng lọc và hiển thị danh sách job.
5. Người dùng chọn thư mục output.
6. Người dùng bấm chuyển đổi.
7. UI hiển thị progress và trạng thái.
8. Người dùng retry job thất bại nếu cần.
9. Người dùng mở thư mục output hoặc clear danh sách.

### 7.2 Hành vi drag-and-drop

- Drop zone phải cho biết rõ có thể thả file vào.
- Khi kéo file hợp lệ qua drop zone, UI có trạng thái hover/active.
- Khi thả thư mục, ứng dụng phải xử lý theo policy đã chọn: quét các file trực tiếp hoặc recursive; quyết định cụ thể phải được chốt ở Phase 0.
- File không hỗ trợ không được đưa vào queue conversion.
- Duplicates phải được loại bỏ hoặc đánh dấu rõ.

### 7.3 Hành vi batch

- Một job lỗi không làm mất các job còn lại.
- Retry chỉ chạy lại job đã failed/cancelled, không tạo duplicate ngoài policy.
- Cancel phải phân biệt job đang chạy và job đang pending.
- Batch summary phải cho biết số lượng thành công, thất bại, bị hủy và bỏ qua.

### 7.4 Thông báo lỗi

Thông báo UI phải:

- Dùng ngôn ngữ dễ hiểu.
- Không chỉ hiển thị exit code.
- Không hiển thị stack trace cho người dùng thông thường.
- Có hướng xử lý khi có thể, ví dụ cài LibreOffice hoặc chọn thư mục có quyền ghi.
- Cho phép mở chi tiết kỹ thuật nếu cần debug ở phiên bản sau.

---

## 8. Cấu trúc repository mục tiêu

```text
Anything2PDF/
├── project-plan.md
├── README.md
├── pyproject.toml
├── .gitignore
├── src/
│   └── anything2pdf/
│       ├── __init__.py
│       ├── __main__.py
│       ├── domain/
│       │   ├── __init__.py
│       │   ├── jobs.py
│       │   ├── formats.py
│       │   ├── errors.py
│       │   └── naming.py
│       ├── application/
│       │   ├── __init__.py
│       │   ├── use_cases.py
│       │   ├── queue.py
│       │   └── events.py
│       ├── infrastructure/
│       │   ├── __init__.py
│       │   ├── libreoffice.py
│       │   ├── processes.py
│       │   ├── filesystem.py
│       │   └── logging.py
│       └── presentation/
│           ├── __init__.py
│           ├── app.py
│           ├── main_window.py
│           ├── models.py
│           └── widgets/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── ui/
│   └── fixtures/
├── scripts/
│   └── build_windows.ps1
├── packaging/
│   └── anything2pdf.spec
└── docs/
    ├── architecture.md
    ├── testing.md
    └── release.md
```

Đây là cấu trúc mục tiêu. Trong Phase 0 có thể điều chỉnh tên file nếu vẫn giữ nguyên boundary và trách nhiệm của từng layer.

---

## 9. Quy trình phát triển theo phase

## Phase 0 - Khởi tạo nền móng

### Mục tiêu

Tạo skeleton có thể chạy, test và lint; đồng thời khóa các contract tối thiểu trước khi xây conversion logic.

### Công việc

1. Tạo package layout theo cấu trúc repository.
2. Tạo `pyproject.toml` với Python 3.12 và dependency groups.
3. Cấu hình pytest, lint, format và type checking phù hợp.
4. Tạo entry point khởi động cửa sổ PySide6 tối thiểu.
5. Định nghĩa supported extension registry.
6. Định nghĩa enum trạng thái và error categories.
7. Viết README setup cho developer.
8. Chốt policy quét thư mục, concurrency mặc định và timeout mặc định.
9. Tạo fixture tối thiểu hoặc ghi rõ cách tạo fixture an toàn.
10. Prototype danh sách job bằng `QTableView`/model, không dùng một widget riêng cho từng job.
11. Đo baseline startup lạnh, RAM idle và kích thước build tối thiểu của PySide6 + Qt Widgets.
12. Ghi lại production dependency, development dependency và dependency không được phép thêm nếu chưa có use case.

### Deliverables

- Project skeleton.
- Cấu hình môi trường.
- App window tối thiểu.
- Test mẫu chạy pass.
- Danh sách quyết định Phase 0.
- Mã nguồn được đẩy lên GitHub.

### Checkpoint P0

- Có thể tạo virtual environment và cài dependency.
- Có thể chạy app skeleton.
- Có thể chạy test suite.
- Lint/format không báo lỗi trong code hiện có.
- Extension và lifecycle contract được ghi lại.
- Concurrency mặc định là 1 và có benchmark baseline cho startup/RAM/build footprint.
- Người dùng cuối không cần cài Python hoặc chạy `pip install` từ bản build thử nghiệm.

### Điều kiện không được chuyển phase

- Chưa thống nhất supported formats.
- Không khởi động được app skeleton.
- Test runner không chạy được.
- Chưa có quyết định về timeout, folder scan hoặc concurrency.

## Phase 1 - Spike LibreOffice và kiểm chứng rủi ro

### Mục tiêu

Xác minh engine thực tế trước khi đầu tư vào queue và UI hoàn chỉnh.

### Công việc

1. Tìm LibreOffice executable trên Windows.
2. Đọc version hoặc xác nhận binary có thể chạy.
3. Chuyển DOCX, PPTX và XLSX fixture bằng CLI.
4. Kiểm tra các định dạng phụ `.doc`, `.odt`, `.ppt`, `.odp`, `.xls`, `.ods` nếu môi trường fixture cho phép.
5. Kiểm tra stdout, stderr và exit code.
6. Kiểm tra input đang bị lock.
7. Kiểm tra output collision.
8. Kiểm tra temporary profile.
9. Kiểm tra timeout và cancel.
10. Kiểm tra các khác biệt layout/font cơ bản.
11. Ghi nhận các vị trí LibreOffice phổ biến và thông báo dependency.

### Deliverables

- Spike script hoặc test có thể lặp lại.
- Kết quả conversion fixture.
- Danh sách error mapping.
- Ghi chú fidelity và known limitations.
- Quyết định engine MVP.

### Checkpoint P1

- Ba nhóm định dạng chính tạo PDF hợp lệ.
- Thiếu LibreOffice tạo lỗi có thể hiểu.
- Timeout/cancel có cách xử lý khả thi.
- Không có blocker khiến engine không phù hợp MVP.

Nếu checkpoint thất bại, phải đánh giá lại engine hoặc thu hẹp supported formats trước khi triển khai UI.

## Phase 2 - Domain và conversion core

### Mục tiêu

Xây pipeline chuyển đổi hoàn chỉnh có thể chạy độc lập với UI.

### Công việc

1. Implement `ConversionJob`.
2. Implement state transition validation.
3. Implement input validation.
4. Implement output naming policy.
5. Implement `ConversionEngine` protocol.
6. Implement `LibreOfficeEngine`.
7. Implement temporary profile isolation.
8. Implement process timeout.
9. Implement process-tree cancel.
10. Implement output temp file và atomic finalize.
11. Implement bounded queue với concurrency mặc định là 1.
12. Implement retry và cancellation semantics.
13. Implement event contract.
14. Đo thời gian, RAM và độ ổn định khi chạy batch tuần tự; chỉ thử concurrency cao hơn như một benchmark, không tự động bật mặc định.
15. Viết unit test và integration test.

### Deliverables

- Domain models.
- Engine adapter.
- Queue/orchestrator.
- Error mapping.
- Test suite cho pipeline không có GUI.

### Checkpoint P2

- Input path được chuyển thành output PDF qua application layer.
- UI chưa cần tham gia để chạy pipeline.
- Unit tests cho domain/queue pass.
- Integration test với LibreOffice pass trên Windows.
- Cancel không để lại output partial theo tiêu chí đã định.

## Phase 3 - GUI MVP

### Mục tiêu

Đưa conversion core vào một workflow desktop trực quan và không block.

### Công việc

1. Tạo main window.
2. Tạo drop zone.
3. Tạo file dialog.
4. Tạo folder dialog.
5. Tạo output selector.
6. Tạo job list model.
7. Render trạng thái và progress.
8. Thêm action convert, retry, cancel, remove và clear.
9. Kết nối application events với Qt signals/slots.
10. Xử lý trạng thái disable/enable của control.
11. Xử lý đóng cửa sổ khi job đang chạy.
12. Hiển thị dependency error.
13. Thêm summary cuối batch.

### Deliverables

- Main window hoàn chỉnh cho MVP.
- Drag-and-drop workflow.
- Batch workflow.
- UI error states.
- UI smoke tests hoặc checklist có thể lặp lại.

### Checkpoint P3

- Kéo-thả nhiều file hoạt động.
- Chọn file và folder hoạt động.
- Chọn output directory hoạt động.
- Convert batch hoạt động.
- Retry và cancel hoạt động.
- UI vẫn phản hồi.
- Không có conversion trực tiếp trên UI thread.

## Phase 4 - Hardening, test và fidelity

### Mục tiêu

Tăng độ tin cậy trước khi build release.

### Công việc

1. Tạo test matrix cho toàn bộ extension MVP.
2. Test Unicode filename và path.
3. Test output collision.
4. Test input không tồn tại và file hỏng.
5. Test file đang mở hoặc bị lock.
6. Test quyền ghi output.
7. Test batch partial failure.
8. Test cancel ở nhiều thời điểm.
9. Test retry sau failure.
10. Test cleanup trong success/failure/cancel.
11. Review log privacy.
12. Review layout/font trên fixture có bảng, ảnh, slide và spreadsheet nhiều trang.
13. Viết known limitations.

### Deliverables

- Test matrix.
- Integration fixture set.
- UI smoke checklist.
- Fidelity report ngắn.
- Privacy/logging review.

### Checkpoint P4

- Test suite pass trong môi trường target.
- Không có lỗi blocker hoặc critical.
- Error message đủ để người dùng xử lý các lỗi phổ biến.
- Temporary files được cleanup trong các flow đã kiểm thử.
- Known limitations được ghi trong tài liệu.

## Phase 5 - Packaging và release candidate

### Mục tiêu

Tạo artifact mà người dùng có thể chạy ngoài môi trường phát triển.

### Công việc

1. Tạo PyInstaller spec.
2. Include package resources và icon.
3. Tạo build script PowerShell.
4. Chạy build onedir.
5. Kiểm tra khởi động từ artifact và đo cold startup/RAM idle.
6. Kiểm tra dependency check LibreOffice.
7. Kiểm tra drag-and-drop từ Windows Explorer.
8. Kiểm tra output path và quyền ghi.
9. Viết hướng dẫn user setup.
10. Viết troubleshooting.
11. Gắn version cho artifact.
12. Ghi lại command build tái tạo được.
13. So sánh artifact với và không có optional theme package nếu có prototype; chỉ giữ package nếu lợi ích UI rõ ràng và footprint chấp nhận được.

### Deliverables

- PyInstaller artifact.
- Build script/spec.
- Release checklist.
- User guide.
- Troubleshooting guide.

### Checkpoint P5

- Artifact chạy trên Windows sạch hoặc môi trường gần sạch.
- Có thể chuyển đổi fixture bằng artifact.
- Thiếu LibreOffice được thông báo đúng.
- Không cần source code để chạy app.
- Build có thể tái tạo.
- Startup và RAM idle đạt baseline đã chốt ở P0 trên máy test đại diện.
- Không có dependency UI bổ sung chưa được đánh giá về footprint và license.

## Phase 6 - Pilot và khóa MVP

### Mục tiêu

Xác nhận sản phẩm với file thực tế và kết thúc scope MVP có kiểm soát.

### Công việc

1. Chạy pilot với bộ tài liệu được phép sử dụng.
2. Phân loại lỗi theo blocker, critical, major và minor.
3. Sửa blocker/critical.
4. Cập nhật fidelity limitations.
5. Chốt supported formats thực tế.
6. Cập nhật README và release notes.
7. Tạo backlog phase tiếp theo.

### Checkpoint P6 - MVP release gate

- Không còn blocker hoặc critical chưa có kế hoạch xử lý.
- Acceptance checklist hoàn tất.
- Test và build artifact pass.
- Tài liệu setup/user/release đồng bộ.
- Scope phiên bản 0.x được khóa.

---

## 10. Chiến lược kiểm thử

### 10.1 Unit test

Unit test không cần LibreOffice hoặc GUI thật khi test các thành phần thuần:

- Supported extension.
- Input validation.
- State transition.
- Collision naming.
- Error mapping.
- Retry policy.
- Cancel state.
- Batch summary.
- Queue scheduling với fake engine.
- Event emission.

### 10.2 Integration test

Integration test chạy trên máy có LibreOffice:

- Locator tìm được executable.
- DOCX conversion.
- PPTX conversion.
- XLSX conversion.
- Các extension phụ nếu fixture có.
- Output PDF tồn tại.
- Output không rỗng và có thể đọc bằng công cụ kiểm tra phù hợp.
- Error khi input hỏng.
- Timeout.
- Temporary profile cleanup.
- Output collision.

Integration tests phụ thuộc LibreOffice phải có marker và hướng dẫn chạy rõ ràng để developer không có engine vẫn chạy được unit suite.

### 10.3 UI smoke test

UI smoke test cần bao phủ:

1. Khởi động ứng dụng.
2. Hiển thị drop zone.
3. Add file qua dialog.
4. Drop nhiều file.
5. Chọn output directory.
6. Start batch.
7. Nhận trạng thái success.
8. Hiển thị failed job.
9. Retry failed job.
10. Cancel running job.
11. Clear completed.
12. Hiển thị missing LibreOffice.

### 10.4 Manual acceptance test

Manual test bắt buộc trước release:

- Kéo file từ Windows Explorer.
- Kéo nhiều file khác loại.
- Kéo file không hỗ trợ.
- Chuyển đổi batch hỗn hợp.
- Output collision.
- Đóng app khi job đang chạy.
- File path có Unicode.
- Thư mục output không có quyền ghi.
- LibreOffice bị thiếu hoặc không chạy được.
- Mở thư mục output sau khi hoàn thành.

### 10.5 Fidelity test

MVP không dùng một con số duy nhất để tuyên bố layout giống Office. Fidelity review tập trung vào:

- PDF có mở được không.
- Nội dung có đầy đủ không.
- Số trang có hợp lý không.
- Text có bị mất hoặc cắt nghiêm trọng không.
- Bảng và hình ảnh có còn không.
- Slide có giữ được kích thước và thứ tự không.
- Spreadsheet có giữ được vùng in cơ bản không.
- Font thay thế có được ghi nhận không.

---

## 11. Logging, privacy và bảo mật dữ liệu

### 11.1 Nguyên tắc privacy

- Không upload input hoặc output.
- Không gọi network trong conversion workflow.
- Không thu thập telemetry trong MVP.
- Không ghi nội dung tài liệu vào log.
- Không ghi toàn bộ command nếu command có thể chứa thông tin path nhạy cảm, hoặc phải sanitize path trước khi log.
- Cleanup temporary profile và output tạm sau mỗi job.

### 11.2 Nội dung log tối thiểu

Có thể log:

- Thời điểm bắt đầu/kết thúc job.
- Job id nội bộ.
- Extension hoặc loại tài liệu.
- Trạng thái cuối.
- Mã lỗi.
- Exit code.
- Thời lượng.
- Thông tin cleanup thành công/thất bại.

Không nên log:

- Nội dung tài liệu.
- Text trích xuất từ tài liệu.
- Dữ liệu nhạy cảm trong tên file nếu không cần thiết.
- Toàn bộ stdout/stderr không được lọc nếu có nguy cơ chứa nội dung nhạy cảm.

### 11.3 File tạm

- Dùng thư mục tạm của hệ điều hành hoặc thư mục tạm do app quản lý.
- Đảm bảo cleanup trên success và failure.
- Cancel phải có cleanup best-effort.
- Nếu cleanup thất bại, cần thông báo kỹ thuật trong log nhưng không làm crash app.

---

## 12. Rủi ro và phương án giảm thiểu

| Rủi ro | Ảnh hưởng | Giảm thiểu |
|---|---|---|
| LibreOffice không cài | Không thể conversion | Dependency check, thông báo cài đặt rõ ràng |
| Khác biệt font | Layout thay đổi | Fixture fidelity, ghi known limitations |
| Khác biệt LibreOffice version | Kết quả không đồng nhất | Ghi version khi debug, test trên môi trường target |
| Office file bị hỏng | Job failure | Validate output, error category, không làm dừng batch |
| File đang bị lock | Conversion failure | Thông báo rõ, retry sau khi đóng file |
| Process không dừng khi cancel | App treo hoặc process mồ côi | Process group/tree termination và test riêng trên Windows |
| Batch quá lớn | CPU/RAM tăng cao | Bounded concurrency, giới hạn queue phù hợp |
| UI block | Trải nghiệm kém | Worker ngoài UI thread và smoke test responsiveness |
| Output ghi đè | Mất dữ liệu | Collision naming, không ghi đè mặc định |
| Path hoặc filename Unicode | Conversion lỗi | Test Unicode và dùng `pathlib`/subprocess đúng cách |
| Quyền ghi output | Job failure | Kiểm tra quyền sớm và message hành động được |
| PyInstaller thiếu resource | Build chạy sai | Smoke test artifact và build checklist |
| Log lộ thông tin | Rủi ro privacy | Log tối thiểu, sanitize và review |
| Phạm vi phình to | Trễ MVP | Checkpoint gate, backlog riêng cho phase sau |

---

## 13. Non-functional requirements

### Hiệu năng

- UI không được block trong thời gian conversion.
- Queue phải giới hạn số job chạy đồng thời; concurrency mặc định là 1.
- Không được tăng concurrency mặc định chỉ dựa trên số core CPU; phải có benchmark CPU, RAM, thời gian hoàn thành và độ ổn định.
- Không đọc toàn bộ nội dung mọi file vào memory trước khi chạy batch.
- Danh sách job phải dùng model/view nhẹ, không tạo một widget nặng cho mỗi file.
- Không dùng QtWebEngine, WebView hoặc preview tài liệu trong MVP.
- Startup lạnh, RAM idle và kích thước artifact phải có baseline từ P0 và được xác minh lại ở P5.
- Không đặt mục tiêu latency cứng vì thời gian phụ thuộc LibreOffice, kích thước và nội dung tài liệu.

### Độ tin cậy

- Một job lỗi không làm crash toàn bộ ứng dụng.
- Một job lỗi không được làm mất input hoặc output hợp lệ của job khác.
- Output partial phải được loại bỏ hoặc không được công bố như output thành công.
- Các trạng thái job phải nhất quán giữa domain, queue và UI.

### Khả năng bảo trì

- Domain có thể test độc lập.
- Engine có thể thay thế qua interface.
- UI không chứa conversion command.
- Supported formats được quản lý tập trung.
- Mỗi module có một trách nhiệm chính.

### Khả năng quan sát

- Người dùng nhìn thấy trạng thái từng job.
- Developer có log đủ để chẩn đoán missing engine, process failure, timeout và output failure.
- Batch summary phải phản ánh đúng kết quả.

### Tương thích

- MVP chỉ cam kết Windows.
- Python 3.12 là runtime được kiểm thử chính.
- LibreOffice phải được kiểm tra trong Phase 1 và được ghi version trong báo cáo release/test khi cần.

---

## 14. Backlog sau MVP

Các hạng mục sau chỉ được xem xét sau khi P6 đạt:

### Ưu tiên cao

- Windows installer hoàn chỉnh.
- Cấu hình thư mục output mặc định.
- Mở rộng test matrix cho các file Office thực tế.
- Cải thiện error details và diagnostic export.
- Hỗ trợ English localization.

### Ưu tiên trung bình

- Watch folder.
- CLI mode.
- Cấu hình PDF nâng cao.
- Profile conversion.
- Chọn concurrency sau khi có benchmark máy yếu và policy bảo vệ tài nguyên.
- History gần đây.

### Cần spike riêng

- Microsoft Office COM engine để tăng fidelity trên Windows.
- Hỗ trợ macOS/Linux.
- Bundle LibreOffice.
- Plugin engine.
- OCR hoặc image-to-PDF.

Mỗi hạng mục mở rộng phải có scope, rủi ro, test strategy và checkpoint riêng trước khi code.

---

## 15. Checklist triển khai

### Trước khi bắt đầu code

- [ ] Xác nhận Windows là target đầu tiên.
- [ ] Xác nhận Python 3.12.
- [ ] Xác nhận PySide6 + Qt Widgets thuần.
- [ ] Xác nhận không dùng QtWebEngine/WebView/UI framework bổ sung trong MVP.
- [ ] Xác nhận LibreOffice cài riêng.
- [ ] Xác nhận danh sách extension MVP.
- [ ] Xác nhận collision naming.
- [ ] Xác nhận offline/no telemetry.
- [ ] Xác nhận PyInstaller onedir.
- [ ] Xác nhận Python runtime và production dependencies được bundle trong artifact.
- [ ] Xác nhận không runtime download Python package hoặc LibreOffice.
- [ ] Xác nhận concurrency mặc định là 1.
- [ ] Xác nhận test layers.

### Trước khi hoàn thành conversion core

- [ ] Domain state machine có test.
- [ ] Validation có test.
- [ ] Collision policy có test.
- [ ] Engine interface tồn tại.
- [ ] LibreOffice adapter không nằm trong UI.
- [ ] Timeout có test.
- [ ] Cancel có test.
- [ ] Output partial được xử lý.
- [ ] Temp cleanup được kiểm tra.

### Trước khi hoàn thành GUI

- [ ] Drag-and-drop hoạt động.
- [ ] File dialog hoạt động.
- [ ] Folder dialog hoạt động.
- [ ] Output selector hoạt động.
- [ ] Job list hiển thị đúng state.
- [ ] Progress được cập nhật.
- [ ] Retry hoạt động.
- [ ] Cancel hoạt động.
- [ ] UI không freeze.
- [ ] Missing LibreOffice có message rõ.

### Trước khi release

- [ ] Unit tests pass.
- [ ] Integration tests pass hoặc được ghi rõ skip vì thiếu dependency.
- [ ] UI smoke pass.
- [ ] Manual acceptance pass.
- [ ] PyInstaller build pass.
- [ ] Artifact chạy ngoài source tree.
- [ ] README được cập nhật.
- [ ] Known limitations được công bố.
- [ ] Không có blocker/critical mở.

---

## 16. Quy tắc cập nhật tài liệu này

`project-plan.md` là nguồn context chính của dự án. Khi phát sinh thay đổi:

1. Xác định thay đổi thuộc product scope, architecture, implementation hoặc release.
2. Đánh giá ảnh hưởng tới phase, checkpoint, test và packaging.
3. Trợ lý trình bày phần muốn sửa, nội dung dự kiến và lý do cho người dùng.
4. Chỉ cập nhật tài liệu sau khi người dùng đồng ý rõ ràng.
5. Không âm thầm thay đổi quyết định đã chốt.
6. Nếu có nhiều phương án, ghi rõ phương án được chọn và lý do.
7. Khi một checkpoint đạt, đề xuất cập nhật trạng thái và evidence; không tự cập nhật nếu chưa được người dùng đồng ý.
8. Code, test, cấu hình và các file khác do người dùng tự cập nhật; plan chỉ ghi nhận quyết định và trạng thái đã được thống nhất.

### 16.1 Nhịp làm việc theo phase

Trước mỗi phase, trợ lý sẽ cung cấp:

- Mục tiêu học tập và mục tiêu kỹ thuật của phase.
- Kiến thức nền cần nắm.
- Các task nhỏ theo thứ tự phụ thuộc.
- File người dùng cần tự tạo hoặc chỉnh.
- Một verification command hoặc manual check cho từng task.
- Tiêu chí checkpoint và dấu hiệu cần dừng để hỏi lại.

Sau mỗi task, người dùng có thể gửi code, lỗi, output test hoặc câu hỏi. Trợ lý sẽ review đúng phạm vi task hiện tại, giải thích nguyên nhân và đề xuất bước sửa. Chỉ khi task đạt checkpoint cục bộ mới chuyển sang task tiếp theo.

### 16.2 Ràng buộc can thiệp file

Trong mọi phase, trợ lý phải giữ nguyên quy tắc sau:

- File duy nhất trợ lý có thể chỉnh là `project-plan.md`.
- Nếu người dùng yêu cầu “implement”, trợ lý phải hiểu là hướng dẫn người dùng tự implement, trừ khi người dùng đưa ra một yêu cầu mới thay đổi rõ ràng working agreement này.
- Nếu phát hiện cần chỉnh file khác để hoàn thành mục tiêu, trợ lý chỉ được chỉ dẫn đường dẫn, nội dung hoặc patch để người dùng tự áp dụng; không được tự gọi công cụ ghi file.
- Việc đọc, phân tích, chạy test hoặc đề xuất command không trao cho trợ lý quyền chỉnh file ngoài `project-plan.md`.

### Trạng thái hiện tại

- [x] Product direction đã được thống nhất.
- [x] MVP scope đã được xác định.
- [x] Tech stack đã được chọn ở mức kế hoạch.
- [x] Kiến trúc layer đã được xác định.
- [x] Phase và checkpoint đã được xác định.
- [x] Working agreement mentor và giới hạn can thiệp file đã được thống nhất.
- [x] Quy trình task-by-task và cơ chế xin phép cập nhật plan đã được ghi nhận.
- [x] Phase 0 - Khởi tạo nền móng đã hoàn thành.
- [ ] Phase 1 - Spike LibreOffice đang chuẩn bị.
- [ ] Phase 2 - Conversion core chưa thực hiện.
- [ ] Phase 3 - GUI MVP chưa thực hiện.
- [ ] Phase 4 - Hardening & release chưa thực hiện.

### Nhật ký tiến độ gần nhất

- **Phase 0 Hoàn tất**:
  - Cấu trúc package, `pyproject.toml`, và entry point PySide6 đã hoạt động.
  - Test runner (pytest) cấu hình thành công với `test_domain.py`.
  - Prototype QTableView với `ConversionJob` đã chạy.
  - Baseline idle RAM ghi nhận ban đầu: 0.5 MB.
  - Đã chốt chính sách xử lý: Concurrency=1, Không quét đệ quy, Timeout=5 phút.
  - Sẵn sàng push code lên GitHub để chuyển sang Phase 1.

- Việc tiếp theo: sửa dòng `requires-python`, sau đó validate metadata và cài development dependencies.

---

## 17. Tóm tắt ngắn cho contributor

Nếu chỉ cần nắm nhanh dự án:

1. Đây là app desktop Windows viết bằng Python 3.12 và PySide6.
2. App nhận DOC/DOCX/ODT, PPT/PPTX/ODP, XLS/XLSX/ODS qua kéo-thả hoặc dialog.
3. App gọi LibreOffice headless để tạo PDF, chạy offline và không ghi đè output.
4. Conversion phải chạy ngoài UI thread qua queue/worker.
5. Domain không phụ thuộc PySide6 hoặc LibreOffice.
6. Engine phải đi qua abstraction.
7. Mọi job phải có state rõ ràng, error category và cleanup.
8. MVP phải pass unit, integration, UI smoke, manual acceptance và PyInstaller artifact test.
9. Không mở rộng sang CLI, watch folder, multi-platform hoặc advanced PDF trước khi checkpoint P6 đạt.
