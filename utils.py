from typing import List
from fastapi import HTTPException


def validaciones_nombre(name:str):
    if len(name)==0:
        raise HTTPException(status_code=400, detail='Debe ingresar un nombre')
    if len(name)>25:
        raise HTTPException(status_code=400, detail='El nombre no debe tener mas de 25 caracteres')
    if len(name)<3:
        raise HTTPException(status_code=400, detail='El nombre debe tener mas de 2 caracteres')
    if not name.isalnum():
        raise HTTPException(status_code=400, detail='El nombre no puede tener caracteres especiales o espacios')


def find_ahorcado(lista_ahorcado:List, nick:str):
    for ahor in lista_ahorcado:
        if ahor.name == nick:
            return ahor
            break
    return None


