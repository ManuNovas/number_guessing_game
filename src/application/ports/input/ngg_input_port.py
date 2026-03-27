from abc import ABC, abstractmethod

from src.domain.entites import Score


class NGGInputPort(ABC):
    @abstractmethod
    def play(self) -> int:
        pass

    @abstractmethod
    def get_high_scores(self) -> list[Score]:
        pass
