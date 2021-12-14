import json

from fastapi import APIRouter
from api.logic.ahorcado_logic import Ahorcado
from utils import find_ahorcado
router = APIRouter()

lista_ahorcado = []


@router.post('/start')
async def start(nick:str):
    '''Inicializamos el juego - devolvemos palabra, vidas'''
    ahorcado = Ahorcado()
    ahorcado.login(name=nick)
    ahorcado.inicializarJuego()
    lista_ahorcado.append(ahorcado)
    return ahorcado

@router.post('/letter')
async def letter(nick:str, letter:str):
    '''Probamos con una letra en la palabra, devolvemos verdadero o falso y el arreglo ordenado'''
    ahorcado = find_ahorcado(lista_ahorcado, nick)
    #Validar ahorcado
    if ahorcado is None:
        return {'respuesta':'no hay tal nick'}
    #Agregar letra
    if ahorcado.validar_letra_repetida(letra=letter):
        ahorcado.agregar_letra(letra=letter)
    else:
        return {'respuesta': 'letra repetida'}
    #Validar finalizacion
    respuesta = ahorcado.validar_finalizacion()
    if respuesta is not False:
        lista_ahorcado.remove(ahorcado)
        return respuesta
    return ahorcado

@router.post('/reset')
async def reset(nick:str):
    '''Resetear el juego'''
    ahorcado = find_ahorcado(lista_ahorcado, nick)
    #Validar ahorcado
    if ahorcado is None:
        return {'respuesta':'no hay tal nick'}
    lista_ahorcado.remove(ahorcado)
    return {'respuesta':'reset completado'}

