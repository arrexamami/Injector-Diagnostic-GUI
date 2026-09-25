from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from app.core.simulator import Simulator
from app.services.diagnosis_service import DiagnosisService
from app.services.ecu_service import EcuService
from app.services.injector_service import InjectorService
from app.ui.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    simulator = Simulator()
    ecu_service = EcuService(simulator)
    injector_service = InjectorService(simulator)
    diagnosis_service = DiagnosisService()

    window = MainWindow(simulator, ecu_service, injector_service, diagnosis_service)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
