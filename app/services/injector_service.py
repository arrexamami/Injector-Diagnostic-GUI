from __future__ import annotations

from app.core.models import InjectorTestType, InjectorTestResult
from app.core.simulator import Simulator


class InjectorService:
    def __init__(self, simulator: Simulator) -> None:
        self.simulator = simulator

    def run_test(self, test_type: InjectorTestType) -> InjectorTestResult:
        return self.simulator.run_injector_test(test_type)
