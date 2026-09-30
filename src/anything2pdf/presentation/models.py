from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from anything2pdf.domain.jobs import ConversionJob

class JoblistModel(QAbstractTableModel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.jobs: list[ConversionJob] = []
        self.headers = ["Tên file", "Trạng thái", "Tiến độ", "Thư mục gốc"]

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.jobs)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.headers)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.jobs)):
            return None

        job = self.jobs[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return job.input_path.name
            elif col == 1:
                return job.state.name
            elif col == 2:
                return f"{job.progress}%"
            elif col == 3:
                return str(job.input_path.parent)

        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.headers[section]
        return None

    def add_job(self, job: ConversionJob):
        """Thêm job mới vào danh sách và thông báo cho UI cập nhật."""
        self.beginInsertRows(QModelIndex(), len(self.jobs), len(self.jobs))
        self.jobs.append(job)
        self.endInsertRows()