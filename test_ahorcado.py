from fastapi.testclient import TestClient
from app import app
import unittest

from models.ahorcado_model import PlayAhorcado_Model
client = TestClient(app)

class TestStart(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.client = TestClient(app)
    def test_leer_main(self)->None:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}

    def test_minlen_3(self)->None:
        nombre = {
            'name': 'xd'
        }
        response = client.post("/start", json=nombre)
        assert response.status_code == 400
        assert response.json() == {"detail": "El nombre debe tener mas de 2 caracteres"}

    def test_maxlen_25(self)->None:
        nombre = {
            'name': 'holamellamoagustinetcheverry'
        }
        response = client.post("/start", json=nombre)
        assert response.status_code == 400
        assert response.json() == {"detail": "El nombre no debe tener mas de 25 caracteres"}

    def test_special_characters(self)->None:
        nombre = {
            'name': '@3hola'
        }
        response = client.post("/start", json=nombre)
        assert response.status_code == 400
        assert response.json() == {"detail": "El nombre no puede tener caracteres especiales o espacios"}

    def test_empty_spaces(self)->None:
        nombre = {
            'name': 'Agustin Etcheverry'
        }
        response = client.post("/start", json=nombre)
        assert response.status_code == 400
        assert response.json() == {"detail": "El nombre no puede tener caracteres especiales o espacios"}
    
    def test_getName(self)->None:
        nombre = {
            'name': 'Agustin'
        }
        response = client.post("/start", json=nombre)
        assert response.status_code == 200
        assert response.json()['name'] == nombre['name']


class TestGame(unittest.TestCase):
    
    def test_initializeVariables(self):
        nombre = {
            'name': 'Agustin'
        }
        response = client.post("/start", json=nombre)
        assert response.status_code == 200
        assert response.json()['vidas'] == 6
        assert response.json()['letras_erroneas'] == []
        assert response.json()['palabra'] != []

    def test_try_letter(self):
        play_ahorcado = {
            'name': 'Agustin',
            'letter': 'a'
        }
        response = client.post("/letter", json=play_ahorcado)
        assert response.status_code == 200
        assert response.json()['name'] == 'Agustin'


    def test_letra_repetida(self):
        nombre = {
            'name': 'Damian'
        }
        response = client.post("/start", json=nombre)
        assert response.status_code == 200
        play_ahorcado = {
            'name': 'Damian',
            'letter': 'a'
        }
        response = client.post("/letter", json=play_ahorcado)
        assert response.status_code == 200
        response = client.post("/letter", json=play_ahorcado)
        assert response.status_code == 200
        assert response.json() == {'detail':'letra repetida'}


    def test_probar_vidas(self):
        nombre = {
            'name': 'Giova'
        }
        response = client.post("/start", json=nombre)
        assert response.status_code == 200
        play_ahorcado = {
            'name': 'Giova',
            'letter': 'x'
        }
        response = client.post("/letter", json=play_ahorcado)
        assert response.status_code == 200
        if play_ahorcado['letter'] in response.json()['letras_erroneas']:
            assert response.json()['vidas'] == 5