from __future__ import annotations

import random
from typing import List

from app.core.models import (
    ConnectionMode,
    CommunicationSettings,
    DtcRecord,
    DtcStatus,
    InjectorTestResult,
    InjectorTestType,
    LiveDataPoint,
    Vehicle,
    EcuSettings,
)


class Simulator:
    def __init__(self) -> None:
        self.vehicle = Vehicle()
        self.ecu = EcuSettings()
        self.communication = CommunicationSettings(mode=ConnectionMode.SIMULATION)
        self._dtcs: List[DtcRecord] = [
            DtcRecord(
                code="P0100",
                system="Air intake",
                description="Mass Air Flow sensor circuit malfunction",
                status=DtcStatus.STORED,
                possible_causes=[
                    "MAF sensor or connector issue",
                    "Wiring/open circuit",
                    "Power or ground problem",
                ],
                recommended_checks=[
                    "Inspect connector and wiring",
                    "Check MAF power/ground",
                    "Compare MAF signal with live data",
                ],
            ),
            DtcRecord(
                code="P0115",
                system="Engine temperature",
                description="Engine coolant temperature sensor circuit malfunction",
                status=DtcStatus.STORED,
                possible_causes=[
                    "ECT sensor fault",
                    "Connector/wiring fault",
                    "Reference or ground issue",
                ],
                recommended_checks=[
                    "Inspect ECT connector",
                    "Check wiring continuity",
                    "Compare temperature reading with engine condition",
                ],
            ),
        ]

    def get_live_data(self) -> List[LiveDataPoint]:
        return [
            LiveDataPoint("RPM", 850.0, "rpm", True, True, 600.0, 9000.0),
            LiveDataPoint("Coolant Temperature", 88.0, "C", True, True, 60.0, 120.0),
            LiveDataPoint("TPS", 12.5, "%", True, True, 0.0, 100.0),
            LiveDataPoint("MAP", 38.0, "kPa", True, True, 0.0, 200.0),
            LiveDataPoint("MAF", 3.2, "g/s", True, True, 0.0, 50.0),
            LiveDataPoint("O2 Sensor", 0.72, "V", True, True, 0.0, 2.0),
            LiveDataPoint("Battery Voltage", 13.9, "V", True, True, 10.0, 15.0),
        ]

    def read_dtc_codes(self) -> List[DtcRecord]:
        return self._dtcs

    def clear_dtc_codes(self) -> None:
        self._dtcs.clear()

    def run_injector_test(self, test_type: InjectorTestType) -> InjectorTestResult:
        if test_type == InjectorTestType.RESISTANCE:
            value = 12.4
            unit = "ohm"
            passed = True
            message = "Simulated resistance is within expected range."
        elif test_type == InjectorTestType.PULSE:
            value = 3.0
            unit = "ms"
            passed = True
            message = "Simulated pulse command accepted."
        elif test_type == InjectorTestType.FLOW:
            value = 105.0
            unit = "mL/min"
            passed = True
            message = "Simulated flow result."
        elif test_type == InjectorTestType.LEAK:
            value = 0.0
            unit = "mL/min"
            passed = True
            message = "Simulated leak test: no leak detected."
        else:
            value = 0.0
            unit = ""
            passed = False
            message = "Unknown test."
        return InjectorTestResult(
            test_type=test_type,
            passed=passed,
            measured_value=value,
            unit=unit,
            message=message,
            simulated=True,
        )

    def update_live_data(self) -> List[LiveDataPoint]:
        live_data = self.get_live_data()
        for point in live_data:
            if point.name == "RPM":
                point.value = random.uniform(780.0, 950.0)
            elif point.name == "Coolant Temperature":
                point.value = random.uniform(82.0, 95.0)
            elif point.name == "TPS":
                point.value = random.uniform(10.0, 18.0)
            elif point.name == "MAP":
                point.value = random.uniform(30.0, 50.0)
            elif point.name == "MAF":
                point.value = random.uniform(2.8, 4.2)
            elif point.name == "O2 Sensor":
                point.value = random.uniform(0.68, 0.85)
            elif point.name == "Battery Voltage":
                point.value = random.uniform(13.4, 14.4)
        return live_data
