from fastapi import APIRouter
from api.logic.ahorcado_logic import Ahorcado
from utils import find_ahorcado
from models.ahorcado_model import base_ahorcado_model, play_ahorcado_model
router = APIRouter()
lista_ahorcado = []

@router.get('/')
def main():
    return {"msg": "Hello World"}

@router.post('/start')
def start(base_ahorcado: base_ahorcado_model):
    '''Inicializamos el juego - devolvemos palabra, vidas'''
    ahorcado = Ahorcado()
    ahorcado.login(name=base_ahorcado.name)
    ahorcado.inicializarJuego()
    lista_ahorcado.append(ahorcado)
    return ahorcado

@router.post('/letter')
def letter(play_ahorcado: play_ahorcado_model):
    '''Probamos con una letra en la palabra, devolvemos verdadero o falso y el arreglo ordenado'''
    ahorcado = find_ahorcado(lista_ahorcado, play_ahorcado.name)
    #Validar ahorcado
    if ahorcado is None:
        return {'detail':'no hay tal nick'}
    #Agregar letra
    if ahorcado.validar_letra_repetida(letra=play_ahorcado.letter):
        ahorcado.agregar_letra(letra=play_ahorcado.letter)
    else:
        return {'detail': 'letra repetida'}
    #Validar finalizacion
    respuesta = ahorcado.validar_finalizacion()
    if respuesta is not False:
        lista_ahorcado.remove(ahorcado)
        return respuesta
    return ahorcado

@router.post('/reset')
def reset(base_ahorcado: base_ahorcado_model):
    '''Resetear el juego'''
    ahorcado = find_ahorcado(lista_ahorcado, base_ahorcado.name)
    #Validar ahorcado
    if ahorcado is None:
        return {'detail':'no hay tal nick'}
    lista_ahorcado.remove(ahorcado)
    return {'detail':'reset completado'}

