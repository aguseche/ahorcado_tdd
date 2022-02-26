'''Imports'''
from typing import List

from pydantic import BaseModel, Field# pylint: disable=no-name-in-module

class BaseAhorcadoModel(BaseModel):# pylint: disable=too-few-public-methods
    '''Clase Base Ahorcado'''
    name:str = Field(None, example="Agustin")

class PlayAhorcadoModel(BaseAhorcadoModel):# pylint: disable=too-few-public-methods
    '''Clase Base Play Ahorcado'''
    letter:str = Field(None, example="a")

class AhoradoModel(BaseModel):# pylint: disable=too-few-public-methods
    '''Clase Ahorcado'''
    name: str
    palabra: str
    vidas: int
    resultado: List
    letras_erroneas: List
