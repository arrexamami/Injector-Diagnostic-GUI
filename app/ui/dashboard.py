from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class StatusCard(QFrame):
    def __init__(self, title: str, value: str, accent: str = "#3AA7FF") -> None:
        super().__init__()
        self.setObjectName("statusCard")
        self.setStyleSheet(
            """
            QFrame#statusCard {
                background: #171B22;
                border: 1px solid #2D3748;
                border-radius: 12px;
            }
            QLabel {
                color: white;
            }
            """
        )
        self.layout = QVBoxLayout(self)
        self.title = QLabel(title)
        self.title.setStyleSheet("color: #A7B1C2; font-size: 12px;")
        self.value = QLabel(value)
        self.value.setStyleSheet(f"color: {accent}; font-size: 22px; font-weight: 600;")
        self.value.setAlignment(Qt.AlignLeft)

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.value)
        self.layout.setContentsMargins(16, 12, 16, 12)


class DashboardWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("dashboard")
        layout = QGridLayout(self)
        layout.setSpacing(14)

        cards = [
            ("ECU Status", "SIMULATION", "#4ADE80"),
            ("OBD/CAN", "CONNECTED", "#60A5FA"),
            ("Battery Voltage", "13.9 V", "#FBBF24"),
            ("RPM", "850 rpm", "#F472B6"),
            ("Engine Temp", "88 C", "#FB7185"),
            ("Faults", "2 DTC", "#F59E0B"),
        ]

        row = 0
        col = 0
        for title, value, accent in cards:
            card = StatusCard(title, value, accent)
            layout.addWidget(card, row, col)
            col += 1
            if col == 3:
                col = 0
                row += 1
