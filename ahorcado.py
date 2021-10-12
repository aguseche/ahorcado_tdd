from utils import validaciones_nombre


class Ahorcado:
    name:str

    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def login(self, name:str)-> None:
        validaciones_nombre(name)
        self.name = name
