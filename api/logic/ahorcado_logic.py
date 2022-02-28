'''Imports'''
import random
from utils import validaciones_nombre

class Ahorcado:
    '''Clase Ahorcado'''
    name:str
    palabra: str
    palabras=["caramelo","auto","salir","pato","puerta"]

    def __init__(self, resultado, letras_erroneas, vidas,palabra,name=None):# pylint: disable=too-many-arguments
        '''init'''
        self.name = name
        self.resultado = resultado
        self.letras_erroneas = letras_erroneas
        self.vidas = vidas
        self.palabra = palabra

    def get_name(self)->str:
        '''get_name'''
        return self.name
    def get_vidas(self)->int:
        '''get_vidas'''
        return  self.vidas

    # methods
    def inicializar_juego(self):
        '''inicializar juego'''
        self.resultado = []
        self.letras_erroneas = []
        self.vidas=6
        self.palabra = list(random.choice(self.palabras))
        for lenght in range(len(self.palabra)):# pylint: disable=unused-variable
            self.resultado.append("_")

    def restar_vida(self)->int:
        '''restar vidas'''
        self.vidas-=1

    def login(self,name)-> None:
        '''login'''
        validaciones_nombre(name)
        self.name = name
    def prueba_letra(self, letra:str)-> bool:
        '''prueba letra'''
        if letra in self.palabra:
            return True
        return False

    def agregar_letra(self, letra:str)-> None:
        '''agregar letra'''
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
        '''validar letra repetida'''
        if (letra in self.resultado) or (letra in self.letras_erroneas):
            return False
        return True

    def validar_finalizacion(self):
        '''validar finalizacion juego'''
        if self.palabra==self.resultado:
            return {'respuesta':'ganaste'}
        if self.vidas==0:
            return {'respuesta':'perdiste'}
        return False
