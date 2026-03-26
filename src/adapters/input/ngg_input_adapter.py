from src.application.ports.input import NGGInputPort


class NGGInputAdapter:
    input_port: NGGInputPort

    def __init__(self, input_port: NGGInputPort):
        self.input_port = input_port

    def main(self):
        close = False
        while not close:
            print("Welcome to the Number Guessing Game!")
            self.input_port.play()
            close_input = input("Would you like to play again? (y/n): ")
            close = close_input.lower() == "n"
        return 0
