from json import dump, load
from os.path import exists

from src.application.ports.output import NGGOutputPort


class NGGOutputAdapter(NGGOutputPort):
    filename: str
    data: list[dict]

    def __init__(self, filename: str):
        self.filename = filename

    def _save(self):
        with open(self.filename, "w") as file:
            dump(self.data, file)

    def _open(self):
        if not exists(self.filename):
            self.data = []
            self._save()
        else:
            with open(self.filename, "r") as file:
                self.data = load(file)
    
    def get_next_id(self) -> int:
        self._open()
        return self.data[-1]["id"] + 1 if len(self.data) > 0 else 1

    def create(self, entity: dict):
        self._open()
        self.data.append(entity)
        self._save()
