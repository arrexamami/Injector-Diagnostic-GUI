from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class ConnectionMode(str, Enum):
    SIMULATION = "SIMULATION"
    HARDWARE = "HARDWARE"


class DtcStatus(str, Enum):
    STORED = "Stored"
    PENDING = "Pending"
    ACTIVE = "Active"


class InjectorTestType(str, Enum):
    RESISTANCE = "Resistance Test"
    PULSE = "Pulse Test"
    FLOW = "Flow Test"
    LEAK = "Leak Test"


@dataclass
class Vehicle:
    manufacturer: str = "BMW"
    model: str = "318i"
    year: int = 2021
    engine: str = "2.0L"
    fuel_type: str = "Petrol"


@dataclass
class EcuSettings:
    manufacturer: str = "Bosch"
    ecu_type: str = "Engine Control Unit"
    protocol: str = "OBD-II"
    communication: str = "CAN"


@dataclass
class CommunicationSettings:
    mode: ConnectionMode = ConnectionMode.SIMULATION
    connection_type: str = "OBD-II"
    port: str = "COM3"
    baud_rate: int = 115200
    status: str = "Disconnected"


@dataclass
class LiveDataPoint:
    name: str
    value: float
    unit: str
    valid: bool = True
    simulated: bool = True
    min_value: Optional[float] = None
    max_value: Optional[float] = None


@dataclass
class DtcRecord:
    code: str
    system: str
    description: str
    status: DtcStatus = DtcStatus.STORED
    possible_causes: List[str] = field(default_factory=list)
    recommended_checks: List[str] = field(default_factory=list)


@dataclass
class InjectorTestResult:
    test_type: InjectorTestType
    passed: bool
    measured_value: float
    unit: str
    message: str
    simulated: bool = True


@dataclass
class DiagnosisStep:
    stage: str
    result: str
    next_action: str
    status: str = "Pending"
