from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class EcuScanWidget(QWidget):
    def __init__(self, ecu_service, simulator=None) -> None:
        super().__init__()
        self.ecu_service = ecu_service
        self.simulator = simulator

        self.root = QVBoxLayout(self)

        self.toolbar = QHBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search DTC / system / description")
        self.scan_button = QPushButton("SCAN ECU")
        self.clear_button = QPushButton("CLEAR DTC")
        self.toolbar.addWidget(self.search_box)
        self.toolbar.addWidget(self.scan_button)
        self.toolbar.addWidget(self.clear_button)
        self.root.addLayout(self.toolbar)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["DTC Code", "System", "Description", "Status", "Fav"])
        self.table.setStyleSheet("QTableWidget { background: #111827; color: white; } QHeaderView::section { background: #1F2937; color: white; }")
        self.root.addWidget(self.table)

        self.info_label = QLabel("Select a DTC to see details.")
        self.info_label.setStyleSheet("color: #A7B1C2; padding: 16px;")
        self.root.addWidget(self.info_label)

        self.scan_button.clicked.connect(self.scan)
        self.clear_button.clicked.connect(self.clear_faults)
        self.search_box.textChanged.connect(self.scan)
        self.table.cellClicked.connect(self.show_details)

    def scan(self) -> None:
        dtcs = self.ecu_service.read_dtc_codes()
        query = self.search_box.text().lower().strip()
        filtered = []
        if query:
            filtered = [
                dtc for dtc in dtcs if query in dtc.code.lower() or query in dtc.system.lower() or query in dtc.description.lower()
            ]
        else:
            filtered = dtcs

        self.table.setRowCount(len(filtered))
        for row, dtc in enumerate(filtered):
            self.table.setItem(row, 0, QTableWidgetItem(dtc.code))
            self.table.setItem(row, 1, QTableWidgetItem(dtc.system))
            self.table.setItem(row, 2, QTableWidgetItem(dtc.description))
            self.table.setItem(row, 3, QTableWidgetItem(dtc.status.value))
            self.table.setItem(row, 4, QTableWidgetItem("★" if dtc.favorite else "☆"))

    def clear_faults(self) -> None:
        self.ecu_service.clear_dtc_codes()
        self.table.setRowCount(0)
        self.info_label.setText("✓ Simulation DTC memory cleared.")
        if self.simulator:
            self.simulator.add_alert("DTC Clearing", "Simulation DTC memory cleared.", "Warning")

    def show_details(self, row: int, col: int) -> None:
        dtcs = self.ecu_service.read_dtc_codes()
        query = self.search_box.text().lower().strip()
        if query:
            dtcs = [
                dtc for dtc in dtcs if query in dtc.code.lower() or query in dtc.system.lower() or query in dtc.description.lower()
            ]
        if row < len(dtcs):
            dtc = dtcs[row]
            self.simulator.add_history_entry(dtc) if self.simulator else None
            text = f"<b>{dtc.code}</b> - {dtc.description}<br>"
            text += f"<b>System:</b> {dtc.system}<br>"
            text += f"<b>Possible Causes:</b><br>"
            for cause in dtc.possible_causes:
                text += f"• {cause}<br>"
            text += f"<b>Recommended Checks:</b><br>"
            for check in dtc.recommended_checks:
                text += f"• {check}<br>"
            self.info_label.setText(text)
