from __future__ import annotations

from app.communication.interface import CommunicationInterface


class CANCommunication(CommunicationInterface):
    def __init__(self, channel: str = "can0") -> None:
        self.channel = channel
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
