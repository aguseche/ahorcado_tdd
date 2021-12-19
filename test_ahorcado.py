import unittest
from api.logic.ahorcado_logic import Ahorcado
from fastapi import HTTPException

class TestLogin(unittest.TestCase):
    def test_nombre_vacio(self):
        ahorcado = Ahorcado()
        try:
            ahorcado.login('')
        except HTTPException as e:
            self.assertTrue('Debe ingresar un nombre',e.detail)
    
    def test_maxlen_25(self):
        ahorcado = Ahorcado()
        try:  
            ahorcado.login('holamellamoagustinetcheverry')
        except HTTPException as e:
            self.assertTrue('El nombre no debe tener mas de 25 caracteres',e.detail)
   
    def test_minlen_3(self):
        ahorcado = Ahorcado()
        try:   
            ahorcado.login('xd')
        except HTTPException as e: 
            self.assertTrue('El nombre debe tener mas de 2 caracteres',e.detail)

    def test_caracteres_especiales(self):
        ahorcado = Ahorcado()
        try:   
            ahorcado.login('@3hola')
        except HTTPException as e: 
            self.assertTrue('El nombre no puede tener caracteres especiales o espacios',e.detail)
    
    def test_espacios_vacios(self):
        ahorcado = Ahorcado()
        try:   
            ahorcado.login('Agustin Etcheverry')
        except HTTPException as e: 
            self.assertTrue('El nombre no puede tener caracteres especiales o espacios',e.detail)
    
    def test_getName(self):
        ahorcado = Ahorcado()
        ahorcado.login('Agustin')
        self.assertEqual('Agustin',ahorcado.get_name())

class TestJuego(unittest.TestCase):
    def test_inicializarVariables(self):
        ahorcado = Ahorcado()
        ahorcado.inicializarJuego()
        self.assertEqual(ahorcado.get_vidas(),6)
        self.assertEqual(ahorcado.letras_erroneas,[])
        self.assertTrue(ahorcado.palabra!=[])

    def test_arriesgo_letra(self):
        ahorcado = Ahorcado()
        ahorcado.inicializarJuego()
        self.assertTrue(ahorcado.prueba_letra('a'))

    def test_letra_repetida(self):
        ahorcado = Ahorcado()
        ahorcado.inicializarJuego()
        ahorcado.agregar_letra('a')        
        self.assertFalse(ahorcado.validar_letra_repetida('a'))

    def test_probar_vidas(self):
        ahorcado = Ahorcado()
        ahorcado.inicializarJuego()
        letra='x'        
        if(not ahorcado.prueba_letra(letra)):
            ahorcado.agregar_letra(letra)                        
            self.assertEqual(ahorcado.get_vidas(),5)

if __name__ == '__main__':
    unittest.main()