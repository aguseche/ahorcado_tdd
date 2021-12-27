from typing import List, Optional

from pydantic import BaseModel, Field

class BaseAhorcado_Model(BaseModel):
    name:str = Field(None, example="Agustin")

class PlayAhorcado_Model(BaseAhorcado_Model):
    letter:str = Field(None, example="a")

class Ahorcado_Model(BaseModel):
    name: str
    palabra: str
    vidas: int
    resultado: List
    letras_erroneas: List