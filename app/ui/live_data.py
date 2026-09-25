from __future__ import annotations

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class LiveDataWidget(QWidget):
    def __init__(self, simulator) -> None:
        super().__init__()
        self.simulator = simulator
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1200)

        self.root = QVBoxLayout(self)
        self.toolbar = QHBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search live values...")
        self.export_button = QPushButton("Export CSV")
        self.export_button.clicked.connect(self.export_csv)
        self.toolbar.addWidget(self.search_box)
        self.toolbar.addWidget(self.export_button)
        self.root.addLayout(self.toolbar)

        self.data_panel = QHBoxLayout()
        self.root.addLayout(self.data_panel)

        self.value_labels = {}
        for name in ["RPM", "Coolant Temperature", "TPS", "MAP", "MAF", "O2 Sensor", "Battery Voltage"]:
            label = QLabel(f"{name}: --")
            label.setStyleSheet("color: white; background: #111827; border-radius: 8px; padding: 8px; font-size: 13px;")
            self.data_panel.addWidget(label)
            self.value_labels[name] = label

    def export_csv(self) -> None:
        result = self.simulator.export_csv("live_data_export.csv")
        self.simulator.add_alert("CSV Export", f"Exported to {result}", "Info")

    def refresh(self) -> None:
        data = self.simulator.update_live_data()
        query = self.search_box.text().lower().strip()
        for point in data:
            if query and query not in point.name.lower():
                continue
            sim_text = " [SIMULATION]" if point.simulated else ""
            self.value_labels[point.name].setText(f"{point.name}: {point.value:.2f} {point.unit}{sim_text}")
