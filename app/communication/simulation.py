from __future__ import annotations

from app.communication.interface import CommunicationInterface
from app.core.simulator import Simulator


class SimulationCommunication(CommunicationInterface):
    def __init__(self) -> None:
        self._connected = False
        self._simulator = Simulator()

    def connect(self) -> bool:
        self._connected = True
        return True

    def disconnect(self) -> None:
        self._connected = False

    def is_connected(self) -> bool:
        return self._connected

    def read_data(self):
        if not self._connected:
            return []
        return self._simulator.update_live_data()
