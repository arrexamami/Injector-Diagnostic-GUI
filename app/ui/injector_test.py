from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.core.models import InjectorTestType


class InjectorTestWidget(QWidget):
    def __init__(self, injector_service, simulator=None) -> None:
        super().__init__()
        self.injector_service = injector_service
        self.simulator = simulator

        self.root = QVBoxLayout(self)
        self.form = QFormLayout()

        self.test_combo = QComboBox()
        self.test_combo.addItems([t.value for t in InjectorTestType])
        self.test_combo.setStyleSheet("QComboBox { background: #111827; color: white; border: 1px solid #374151; padding: 6px; border-radius: 6px; }")
        self.form.addRow("Test Type", self.test_combo)

        self.result_label = QLabel("Waiting for test...")
        self.result_label.setStyleSheet("color: #A7B1C2; padding: 12px; background: #111827; border-radius: 8px;")
        self.form.addRow("Result", self.result_label)

        self.run_button = QPushButton("Run Test")
        self.run_button.setStyleSheet("QPushButton { background: #2563EB; color: white; padding: 10px; border-radius: 8px; font-weight: 600; }")
        self.run_button.clicked.connect(self.run_test)

        self.batch_button = QPushButton("Run Batch Tests")
        self.batch_button.setStyleSheet("QPushButton { background: #0EA5E9; color: white; padding: 10px; border-radius: 8px; font-weight: 600; }")
        self.batch_button.clicked.connect(self.run_batch)

        self.root.addLayout(self.form)
        self.root.addWidget(self.run_button)
        self.root.addWidget(self.batch_button)
        self.root.addStretch()

    def run_test(self) -> None:
        value = self.test_combo.currentText()
        test_type = InjectorTestType(value)
        result = self.injector_service.run_test(test_type)
        status = "✓ PASS" if result.passed else "✗ FAIL"
        self.result_label.setText(
            f"<b>{result.test_type.value}</b>: {status}<br>"
            f"Measured: {result.measured_value} {result.unit}<br>"
            f"Message: {result.message}<br>"
            f"<font color='#FBBF24'>[SIMULATION]</font>"
        )
        if self.simulator:
            self.simulator.add_alert("Injector Test", f"{result.test_type.value} completed.", "Info")

    def run_batch(self) -> None:
        if self.simulator:
            tests = self.simulator.run_batch_tests()
            summary = "<br>".join(f"{item.test_type.value}: {'PASS' if item.passed else 'FAIL'}" for item in tests)
            self.result_label.setText(summary)
            self.simulator.add_alert("Batch Test", "All injector tests completed in simulation mode.", "Info")
