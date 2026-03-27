from src.application.ports.input import NGGInputPort


class NGGInputAdapter:
    input_port: NGGInputPort

    def __init__(self, input_port: NGGInputPort):
        self.input_port = input_port

    def main(self):
        print("Welcome to the Number Guessing Game!")
        print("")
        print("1. Play")
        print("2. High scores")
        print("")
        option = input("Chose an option: ")
        match option:
            case "1":
                close = False
                while not close:
                    self.input_port.play()
                    close_input = input("Would you like to play again? (y/n): ")
                    close = close_input.lower() == "n"
            case "2":
                high_scores = self.input_port.get_high_scores()
                i = 1
                for high_score in high_scores:
                    print(f"{str(i)}. Difficulty: {high_score.get_difficulty_label()}\tAttempts: {str(high_score.attempts)}\tTime: {high_score.time}")
                    i += 1
        return 0
