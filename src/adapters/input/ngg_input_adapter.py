from src.application.ports.input import NGGInputPort


class NGGInputAdapter:
    input_port: NGGInputPort

    def __init__(self, input_port: NGGInputPort):
        self.input_port = input_port

    def main(self):
        print("Welcome to the Number Guessing Game!")
        self.input_port.play()
