class Score:
    id: int
    difficulty: int
    attempts: int
    time: str

    def __init__(self, id: int, difficulty: int, attempts: int, time: str):
        self.id = id
        self.difficulty = difficulty
        self.attempts = attempts
        self.time = time
