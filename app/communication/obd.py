from __future__ import annotations

from app.communication.interface import CommunicationInterface


class OBDCommunication(CommunicationInterface):
    def __init__(self, port: str = "COM3", baud_rate: int = 115200) -> None:
        self.port = port
        self.baud_rate = baud_rate
        self._connected = False

    def connect(self) -> bool:
        self._connected = True
        return True

    def disconnect(self) -> None:
        self._connected = False

    def is_connected(self) -> bool:
        return self._connected

    def read_data(self):
        return []
