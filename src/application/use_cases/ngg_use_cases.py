from random import randrange

from src.application.ports.input import NGGInputPort


class NGGUseCases(NGGInputPort):
    def play(self):
        print("I'm thinking of a number between 1 and 100.")
        number = randrange(1, 100)
        print("You have 5 chances to guess the correct number.")
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
        print("Let's start the game!")
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
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                return 200
            attempts += 1
        print(f"Game over! The number was {str(number)}")
        return 202

