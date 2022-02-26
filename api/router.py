'''Imports'''
from fastapi import APIRouter

from api.endpoints import ahorcado_endpoint


api_router = APIRouter()
api_router.include_router(ahorcado_endpoint.router)
