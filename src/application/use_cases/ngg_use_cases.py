from random import randrange

from src.domain.entites import Score
from src.application.ports.input import NGGInputPort


class NGGUseCases(NGGInputPort):
    score: Score

    def __init__(self):
        self.score = Score()

    def start(self):
        self.score.number = randrange(1, 100)
