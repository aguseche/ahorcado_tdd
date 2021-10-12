from utils import validaciones_nombre


class Ahorcado:
    name:str
    palabra: str 
    letras_correctas = []
    letras_erroneas = []

    def __init__(self):
        self.name = None
        self.palabra = "agustin"
        for l in self.palabra:
            self.letras_correctas.append("_")

    def get_name(self):
        return self.name

    def login(self, name:str)-> None:
        validaciones_nombre(name)
        self.name = name
    
    def prueba_letra(self, letra:str)-> bool:
        if letra in self.palabra:
            return True
        return False

    def agregar_letra(self, letra:str)-> None:
        if self.validar_letra_repetida(letra):
            if self.prueba_letra(letra=letra):
                posiciones = []
                for pos,char in enumerate(self.palabra):
                    if(char == letra):
                        posiciones.append(pos)
                for pos in posiciones:
                    self.letras_correctas[pos] = letra
                #print('Correcto !')
            else:
                self.letras_erroneas.append(letra)
                print('Oops :(')
        else:
            print('No puede repetir letras')

    def validar_letra_repetida(self, letra:str)->bool:
        if (letra in self.letras_correctas) or (letra in self.letras_erroneas):
            return False
        return True

    def validar_finalizacion(self):
        for p in self.palabra:
            if self.letras_correctas[p] == '_':
                break
        print("Ganasteee !!!! :) :D")

    def jugar(self):
        print('Bienvenido, ingrese su nombre: ')
        name = input()
        self.login(name = name)
        letra = " "
        while(letra != '.'):
            print('ingrese una letra: (. para salir) ')
            letra = input()
            self.agregar_letra(letra)
            print(self.letras_correctas)
            print(self.letras_erroneas)
            print("/************************/")


if __name__ == '__main__':
    ahorcado = Ahorcado()
    ahorcado.jugar()

