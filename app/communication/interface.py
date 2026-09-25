from __future__ import annotations

from abc import ABC, abstractmethod


class CommunicationInterface(ABC):
    @abstractmethod
    def connect(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def is_connected(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def read_data(self):
        raise NotImplementedError
