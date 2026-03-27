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

    def get_difficulty_label(self):
        match self.difficulty:
            case 1:
                label = "Easy"
            case 2:
                label = "Medium"
            case 3:
                label = "Hard"
            case _:
                label = "N/A"
        return label
