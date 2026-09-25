from __future__ import annotations

import csv
import random
from datetime import datetime
from typing import List

from app.core.models import (
    ConnectionMode,
    CommunicationSettings,
    DtcHistoryEntry,
    DtcRecord,
    DtcStatus,
    InjectorTestResult,
    InjectorTestType,
    LiveDataPoint,
    Vehicle,
    EcuSettings,
    LoggedSample,
    WorkSession,
    Alert,
)


class Simulator:
    def __init__(self) -> None:
        self.vehicle = Vehicle()
        self.ecu = EcuSettings()
        self.communication = CommunicationSettings(mode=ConnectionMode.SIMULATION)
        self.theme = "Dark"
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
                favorite=True,
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
        self.history: List[DtcHistoryEntry] = []
        self.samples: List[LoggedSample] = []
        self.alerts: List[Alert] = []
        self.sessions: List[WorkSession] = []
        self.favorites: List[str] = ["P0100"]

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
        self.history.clear()
        self.alerts.append(Alert("DTC Cleared", "Simulation DTC memory cleared.", "Info"))

    def add_history_entry(self, dtc: DtcRecord) -> None:
        self.history.append(
            DtcHistoryEntry(
                code=dtc.code,
                system=dtc.system,
                description=dtc.description,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )
        )

    def add_to_favorites(self, dtc_code: str) -> None:
        if dtc_code not in self.favorites:
            self.favorites.append(dtc_code)
        for dtc in self._dtcs:
            if dtc.code == dtc_code:
                dtc.favorite = True

    def remove_from_favorites(self, dtc_code: str) -> None:
        if dtc_code in self.favorites:
            self.favorites.remove(dtc_code)
        for dtc in self._dtcs:
            if dtc.code == dtc_code:
                dtc.favorite = False

    def get_history(self) -> List[DtcHistoryEntry]:
        return self.history

    def add_alert(self, title: str, message: str, level: str = "Info") -> None:
        self.alerts.append(Alert(title, message, level))

    def get_alerts(self) -> List[Alert]:
        return self.alerts

    def log_sample(self, point: LiveDataPoint) -> None:
        self.samples.append(
            LoggedSample(
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name=point.name,
                value=point.value,
                unit=point.unit,
            )
        )

    def export_csv(self, path: str) -> str:
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "name", "value", "unit"])
            for sample in self.samples:
                writer.writerow([sample.timestamp, sample.name, sample.value, sample.unit])
        return path

    def create_session(self, name: str) -> WorkSession:
        session = WorkSession(
            session_id=f"session-{len(self.sessions) + 1}",
            name=name,
            vehicle=f"{self.vehicle.manufacturer} {self.vehicle.model}",
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            notes="Simulation session",
        )
        self.sessions.append(session)
        return session

    def get_sessions(self) -> List[WorkSession]:
        return self.sessions

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
        for point in live_data:
            self.log_sample(point)
        if len(self.samples) > 200:
            self.samples = self.samples[-200:]
        return live_data

    def run_batch_tests(self) -> List[InjectorTestResult]:
        return [self.run_injector_test(test_type) for test_type in InjectorTestType]

    def set_theme(self, theme: str) -> None:
        self.theme = theme

    def toggle_theme(self) -> str:
        self.theme = "Light" if self.theme == "Dark" else "Dark"
        return self.theme
