'''Imports'''
from utils import validaciones_nombre
import random

class Ahorcado:
    '''Clase Ahorcado'''
    name:str
    palabra: str
    palabras=["caramelo","auto","salir","pato","puerta"]
    def __init__(self):
        '''init'''
        self.name = None
    def get_name(self)->str:
        '''get_name'''
        return self.name
    def get_vidas(self)->int:
        '''get_vidas'''
        return  self.vidas

    # methods
    def inicializarJuego(self):
        self.resultado = []
        self.letras_erroneas = []
        self.vidas=6
        self.palabra = list(random.choice(self.palabras))
        for l in range(len(self.palabra)):
            self.resultado.append("_")

    def restar_vida(self)->int:
        self.vidas-=1

    def login(self,name)-> None:
        validaciones_nombre(name)
        self.name = name
    def prueba_letra(self, letra:str)-> bool:
        if letra in self.palabra:
            return True
        return False

    def agregar_letra(self, letra:str)-> None:
        if self.prueba_letra(letra=letra):
            posiciones = []
            for pos,char in enumerate(self.palabra):
                if char == letra:
                    posiciones.append(pos)
            for pos in posiciones:
                self.resultado[pos] = letra
        else:
            self.restar_vida()
            self.letras_erroneas.append(letra)

    def validar_letra_repetida(self, letra:str)->bool:
        if (letra in self.resultado) or (letra in self.letras_erroneas):
            return False
        return True

    def validar_finalizacion(self):
        if self.palabra==self.resultado:
            return {'respuesta':'ganaste'}
        if self.vidas==0:
            return {'respuesta':'perdiste'}
        return False
