from random import randrange
from time import time, gmtime, strftime

from src.domain.entites import Score
from src.application.ports.input import NGGInputPort
from src.application.ports.output import NGGOutputPort


class NGGUseCases(NGGInputPort):
    output_port: NGGOutputPort

    def __init__(self, output_port: NGGOutputPort):
        self.output_port = output_port

    def play(self):
        print("I'm thinking of a number between 1 and 100.")
        number = randrange(1, 100)
        print("")
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        print("")
        difficulty_input = input("Enter your choice: ")
        difficulty = int(difficulty_input)
        if difficulty < 1 or difficulty > 4:
            print("Invalid difficulty")
            return 400
        print("")
        if difficulty == 1:
            difficulty_label = "Easy"
            max_attempts = 10
        elif difficulty == 2:
            difficulty_label = "Medium"
            max_attempts = 5
        else:
            difficulty_label = "Hard"
            max_attempts = 3
        print(f"Great! You have selected the {difficulty_label} difficulty level.")
        print(f"You have {str(max_attempts)} chances to guess the correct number.")
        print("Let's start the game!")
        start_time = time()
        print("")
        attempts = 1
        while attempts <= max_attempts:
            guess_input = input("Enter your guess: ")
            guess = int(guess_input)
            if number < guess:
                print(f"Incorrect! The number is less than {guess}")
            elif number > guess:
                print(f"Incorrect! The number is greater than {guess}")
            else:
                guess_time = time() - start_time
                gm_time = gmtime(guess_time)
                format_time = strftime("%H:%M:%S", gm_time)
                print(f"Congratulations! You guessed the correct number in {attempts} attempts at {format_time}.")
                score = Score(
                    id=self.output_port.get_next_id(),
                    difficulty=difficulty,
                    attempts=attempts,
                    time=format_time,
                )
                self.output_port.create(score.__dict__)
                return 200
            attempts += 1
        print(f"Game over! The number was {str(number)}")
        return 202
    
    def get_high_scores(self) -> list[Score]:
        entities = self.output_port.sort_by("attempts", "asc")
        i = 0
        scores = []
        for entity in entities:
            if i < 3:
                score = Score(
                    id=entity["id"],
                    difficulty=entity["difficulty"],
                    attempts=entity["attempts"],
                    time=entity["time"],
                )
                scores.append(score)
            else:
                break
            i += 1
        return scores
