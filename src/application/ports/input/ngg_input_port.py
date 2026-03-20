from abc import ABC, abstractmethod


class NGGInputPort(ABC):
    @abstractmethod
    def start(self):
        pass
