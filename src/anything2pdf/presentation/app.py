import sys, uuid
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView,QVBoxLayout, QWidget
from anything2pdf.presentation.models import JoblistModel
from anything2pdf.domain.jobs import ConversionJob, JobState

def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Anything2PDF - Phase 0 Prototype")
    window.resize(800, 400)

    table_view = QTableView()
    model = JoblistModel()
    table_view.setModel(model)

    table_view.horizontalHeader().setStretchLastSection(True)

    table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

    fake_job_1 = ConversionJob(
        id=uuid.uuid4(),
        input_path=Path("C:/TaiLieu/BaoGia_2026.docx"),
        output_dir=Path("C:/TaiLieu/PDF_Output"),
        state=JobState.PENDING
    )
    fake_job_2 = ConversionJob(
        id=uuid.uuid4(),
        input_path=Path("C:/TaiLieu/ThongKe_Q1.xlsx"),
        output_dir=Path("C:/TaiLieu/PDF_Output"),
        state=JobState.RUNNING,
        progress=45
    )

    model.add_job(fake_job_1)
    model.add_job(fake_job_2)

    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    layout.addWidget(table_view)
    window.setCentralWidget(central_widget)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()