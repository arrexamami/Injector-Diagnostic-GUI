from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from app.core.models import ConnectionMode


class SettingsWidget(QWidget):
    def __init__(self, simulator) -> None:
        super().__init__()
        self.simulator = simulator

        self.root = QVBoxLayout(self)
        self.form = QFormLayout()

        self.vehicle_input = QLineEdit(self.simulator.vehicle.manufacturer)
        self.form.addRow("Vehicle", self.vehicle_input)

        self.model_input = QLineEdit(self.simulator.vehicle.model)
        self.form.addRow("Model", self.model_input)

        self.year_input = QSpinBox()
        self.year_input.setValue(self.simulator.vehicle.year)
        self.form.addRow("Year", self.year_input)

        self.ecu_input = QLineEdit(self.simulator.ecu.ecu_type)
        self.form.addRow("ECU Type", self.ecu_input)

        self.mode_combo = QComboBox()
        self.mode_combo.addItems([m.value for m in ConnectionMode])
        self.form.addRow("Mode", self.mode_combo)

        self.port_input = QLineEdit(self.simulator.communication.port)
        self.form.addRow("COM Port", self.port_input)

        self.baud_input = QSpinBox()
        self.baud_input.setValue(self.simulator.communication.baud_rate)
        self.form.addRow("Baud Rate", self.baud_input)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Dark", "Light"])
        self.theme_combo.setCurrentText(self.simulator.theme)
        self.form.addRow("Theme", self.theme_combo)

        self.root.addLayout(self.form)
        self.apply_button = QPushButton("Apply Settings")
        self.apply_button.clicked.connect(self.apply_settings)
        self.root.addWidget(self.apply_button)

    def apply_settings(self) -> None:
        self.simulator.vehicle.manufacturer = self.vehicle_input.text()
        self.simulator.vehicle.model = self.model_input.text()
        self.simulator.vehicle.year = self.year_input.value()
        self.simulator.ecu.ecu_type = self.ecu_input.text()
        self.simulator.communication.port = self.port_input.text()
        self.simulator.communication.baud_rate = self.baud_input.value()
        self.simulator.set_theme(self.theme_combo.currentText())
