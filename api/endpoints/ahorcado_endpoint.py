import json

from fastapi import APIRouter, HTTPException
from api.logic.ahorcado_logic import Ahorcado
from utils import find_ahorcado

from models.ahorcado_model import BaseAhorcado_Model, PlayAhorcado_Model

router = APIRouter()

lista_ahorcado = []

@router.get('/')
async def main():
    return {"msg": "Hello World"}

@router.post('/start')
async def start(baseAhorcado: BaseAhorcado_Model):
    '''Inicializamos el juego - devolvemos palabra, vidas'''
    ahorcado = Ahorcado()
    ahorcado.login(name=baseAhorcado.name)
    ahorcado.inicializarJuego()
    lista_ahorcado.append(ahorcado)
    return ahorcado

@router.post('/letter')
async def letter(playAhorcado: PlayAhorcado_Model):
    '''Probamos con una letra en la palabra, devolvemos verdadero o falso y el arreglo ordenado'''
    ahorcado = find_ahorcado(lista_ahorcado, playAhorcado.name)
    #Validar ahorcado
    if ahorcado is None:
        return {'detail':'no hay tal nick'}
    #Agregar letra
    if ahorcado.validar_letra_repetida(letra=playAhorcado.letter):
        ahorcado.agregar_letra(letra=playAhorcado.letter)
    else:
        return {'detail': 'letra repetida'}
    #Validar finalizacion
    respuesta = ahorcado.validar_finalizacion()
    if respuesta is not False:
        lista_ahorcado.remove(ahorcado)
        return respuesta
    return ahorcado

@router.post('/reset')
async def reset(baseAhorcado: BaseAhorcado_Model):
    '''Resetear el juego'''
    ahorcado = find_ahorcado(lista_ahorcado, nick)
    #Validar ahorcado
    if ahorcado is None:
        return {'detail':'no hay tal nick'}
    lista_ahorcado.remove(ahorcado)
    return {'detail':'reset completado'}

