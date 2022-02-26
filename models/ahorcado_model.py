from typing import List, Optional

from pydantic import BaseModel, Field

class base_ahorcado_model(BaseModel):
    name:str = Field(None, example="Agustin")

class play_ahorcado_model(base_ahorcado_model):
    letter:str = Field(None, example="a")

class ahorcado_model(BaseModel):
    name: str
    palabra: str
    vidas: int
    resultado: List
    letras_erroneas: List
