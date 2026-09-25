from __future__ import annotations

from PySide6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QWidget,
    QVBoxLayout,
)

from app.ui.dashboard import DashboardWidget
from app.ui.diagnosis import DiagnosisWidget
from app.ui.ecu_scan import EcuScanWidget
from app.ui.injector_test import InjectorTestWidget
from app.ui.live_data import LiveDataWidget
from app.ui.settings import SettingsWidget


class MainWindow(QMainWindow):
    def __init__(self, simulator, ecu_service, injector_service, diagnosis_service) -> None:
        super().__init__()
        self.setWindowTitle("INJECTOR DIAGNOSTIC")
        self.resize(1200, 800)
        self.setStyleSheet("""
            QWidget {
                background: #0F172A;
                color: #E5E7EB;
                font-family: "Segoe UI", sans-serif;
                font-size: 11px;
            }
            QTabWidget::pane {
                border: 1px solid #1F2937;
                background: #111827;
            }
            QTabBar::tab {
                background: #111827;
                color: #D1D5DB;
                padding: 10px 20px;
                border: 1px solid #374151;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: #1F2937;
                color: #FFFFFF;
                border-bottom: 2px solid #2563EB;
            }
            QPushButton {
                background: #2563EB;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: #1D4ED8;
            }
            QPushButton:pressed {
                background: #1E40AF;
            }
            QTableWidget {
                background: #111827;
                color: white;
                gridline-color: #374151;
                border: 1px solid #374151;
            }
            QHeaderView::section {
                background: #1F2937;
                color: white;
                padding: 8px;
                border: 1px solid #374151;
            }
            QLabel {
                color: white;
            }
            QLineEdit, QSpinBox, QComboBox {
                background: #111827;
                color: white;
                border: 1px solid #374151;
                padding: 6px;
                border-radius: 6px;
            }
        """)

        central = QWidget(self)
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        tabs = QTabWidget()
        tabs.addTab(DashboardWidget(), "Dashboard")
        tabs.addTab(LiveDataWidget(simulator), "Live Data")
        tabs.addTab(EcuScanWidget(ecu_service), "ECU Scan")
        tabs.addTab(InjectorTestWidget(injector_service), "Injector Test")
        tabs.addTab(DiagnosisWidget(diagnosis_service, ecu_service), "Diagnosis")
        tabs.addTab(SettingsWidget(simulator), "Settings")

        layout.addWidget(tabs)
