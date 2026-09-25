from __future__ import annotations

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from app.core.models import LiveDataPoint


class LiveDataWidget(QWidget):
    def __init__(self, simulator) -> None:
        super().__init__()
        self.simulator = simulator
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

        self.root = QVBoxLayout(self)
        self.data_panel = QHBoxLayout()
        self.root.addLayout(self.data_panel)

        self.value_labels = {}
        for name in ["RPM", "Coolant Temperature", "TPS", "MAP", "MAF", "O2 Sensor", "Battery Voltage"]:
            label = QLabel(f"{name}: --")
            label.setStyleSheet("color: white; background: #111827; border-radius: 8px; padding: 8px; font-size: 13px;")
            self.data_panel.addWidget(label)
            self.value_labels[name] = label

    def refresh(self) -> None:
        data = self.simulator.update_live_data()
        for point in data:
            sim_text = " [SIMULATION]" if point.simulated else ""
            self.value_labels[point.name].setText(f"{point.name}: {point.value:.2f} {point.unit}{sim_text}")
