from abc import ABC, abstractmethod


class NGGInputPort(ABC):
    @abstractmethod
    def play(self) -> int:
        pass
