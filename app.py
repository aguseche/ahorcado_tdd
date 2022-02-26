'''Imports'''
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router

app = FastAPI(
  title="FastAPI - Ahorcado",
  description="Aplicacion de ahorcado",
  version="0.0.1"
)

app.include_router(api_router)

# CORS (conectarse desde el front)
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

#Debug
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
