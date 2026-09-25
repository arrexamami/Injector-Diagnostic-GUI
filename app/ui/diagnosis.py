from __future__ import annotations

from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.core.models import DtcRecord


class DiagnosisWidget(QWidget):
    def __init__(self, diagnosis_service, ecu_service, simulator=None) -> None:
        super().__init__()
        self.diagnosis_service = diagnosis_service
        self.ecu_service = ecu_service
        self.simulator = simulator
        self.root = QVBoxLayout(self)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search diagnosis workflow")
        self.root.addWidget(self.search_box)

        self.info = QLabel("Select a DTC to start diagnosis workflow.")
        self.info.setStyleSheet("color: #A7B1C2; padding: 16px; background: #111827; border-radius: 8px;")
        self.root.addWidget(self.info)

        self.load_button = QPushButton("Load Available DTCs")
        self.load_button.setStyleSheet("QPushButton { background: #2563EB; color: white; padding: 10px; border-radius: 8px; }")
        self.load_button.clicked.connect(self.load_dtcs)
        self.root.addWidget(self.load_button)
        self.root.addStretch()

    def load_dtcs(self) -> None:
        dtcs = self.ecu_service.read_dtc_codes()
        if dtcs:
            self.show_dtc(dtcs[0])
        else:
            self.info.setText("No DTCs found.")

    def show_dtc(self, dtc: DtcRecord) -> None:
        steps = self.diagnosis_service.create_workflow(dtc)
        text = f"<b>Diagnosis Workflow for {dtc.code}</b><br><br>"
        for i, step in enumerate(steps, 1):
            status_color = "#4ADE80" if step.status == "Passed" else "#FBBF24" if step.status == "Pending" else "#F87171"
            text += f"<b>{i}. {step.stage}</b> <font color='{status_color}'>({step.status})</font><br>"
            text += f"Result: {step.result}<br>"
            text += f"Next: {step.nextAction}<br><br>"
        self.info.setText(text)
