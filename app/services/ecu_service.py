from __future__ import annotations

from typing import List

from app.core.models import DtcRecord, CommunicationSettings, ConnectionMode
from app.core.simulator import Simulator


class EcuService:
    def __init__(self, simulator: Simulator) -> None:
        self.simulator = simulator

    def get_status_text(self, communication: CommunicationSettings) -> str:
        if communication.mode == ConnectionMode.SIMULATION:
            return "SIMULATION MODE"
        if communication.status == "Connected":
            return "CONNECTED"
        return "DISCONNECTED"

    def read_dtc_codes(self) -> List[DtcRecord]:
        return self.simulator.read_dtc_codes()

    def clear_dtc_codes(self) -> None:
        self.simulator.clear_dtc_codes()
