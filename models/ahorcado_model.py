'''Imports'''
from typing import List

from pydantic import BaseModel, Field# pylint: disable=no-name-in-module

class BaseAhorcadoModel(BaseModel):# pylint: disable=too-few-public-methods
    '''Clase Base Ahorcado'''
    name:str = Field(None, example="Agustin")

class AhorcadoModel(BaseModel):# pylint: disable=too-few-public-methods
    '''Clase Ahorcado'''
    name: str =Field(example="Agustin")
    palabra: str=Field(example="pato")
    vidas: int=Field(example="6")
    resultado: List=Field(example=["_","_","_","_"])
    letras_erroneas: List=Field(example=[])

class PlayAhorcadoModel(AhorcadoModel):# pylint: disable=too-few-public-methods
    '''Clase Base Play Ahorcado'''
    letter:str = Field(None, example="a")


