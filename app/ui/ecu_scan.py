from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.core.models import DtcRecord


class EcuScanWidget(QWidget):
    def __init__(self, ecu_service) -> None:
        super().__init__()
        self.ecu_service = ecu_service

        self.root = QVBoxLayout(self)

        self.header = QHBoxLayout()
        self.scan_button = QPushButton("SCAN ECU")
        self.clear_button = QPushButton("CLEAR DTC")
        self.header.addWidget(self.scan_button)
        self.header.addWidget(self.clear_button)
        self.root.addLayout(self.header)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["DTC Code", "System", "Description", "Status"])
        self.table.setStyleSheet("QTableWidget { background: #111827; color: white; } QHeaderView::section { background: #1F2937; color: white; }")
        self.root.addWidget(self.table)

        self.info_label = QLabel("Select a DTC to see details.")
        self.info_label.setStyleSheet("color: #A7B1C2; padding: 16px;")
        self.root.addWidget(self.info_label)

        self.scan_button.clicked.connect(self.scan)
        self.clear_button.clicked.connect(self.clear_faults)
        self.table.cellClicked.connect(self.show_details)

    def scan(self) -> None:
        dtcs = self.ecu_service.read_dtc_codes()
        self.table.setRowCount(len(dtcs))
        for row, dtc in enumerate(dtcs):
            self.table.setItem(row, 0, QTableWidgetItem(dtc.code))
            self.table.setItem(row, 1, QTableWidgetItem(dtc.system))
            self.table.setItem(row, 2, QTableWidgetItem(dtc.description))
            self.table.setItem(row, 3, QTableWidgetItem(dtc.status.value))

    def clear_faults(self) -> None:
        self.ecu_service.clear_dtc_codes()
        self.table.setRowCount(0)
        self.info_label.setText("✓ Simulation DTC memory cleared.")

    def show_details(self, row: int, col: int) -> None:
        dtcs = self.ecu_service.read_dtc_codes()
        if row < len(dtcs):
            dtc = dtcs[row]
            text = f"<b>{dtc.code}</b> - {dtc.description}<br>"
            text += f"<b>System:</b> {dtc.system}<br>"
            text += f"<b>Possible Causes:</b><br>"
            for cause in dtc.possible_causes:
                text += f"• {cause}<br>"
            text += f"<b>Recommended Checks:</b><br>"
            for check in dtc.recommended_checks:
                text += f"• {check}<br>"
            self.info_label.setText(text)
