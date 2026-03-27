from abc import ABC, abstractmethod


class NGGOutputPort(ABC):
    @abstractmethod
    def get_next_id(self) -> int:
        pass

    @abstractmethod
    def create(self, entity: dict):
        pass
