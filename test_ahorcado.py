import unittest
from ahorcado import Ahorcado

class TestLogin(unittest.TestCase):
    def test_nombre_vacio(self):
        ahorcado = Ahorcado()
        with self.assertRaises(Exception) as context:    
            ahorcado.login('')
        self.assertTrue('Debe ingresar un nombre' in str(context.exception))
    
    def test_maxlen_25(self):
        ahorcado = Ahorcado()
        with self.assertRaises(Exception) as context:    
            ahorcado.login('holamellamoagustinetcheverry')
        self.assertTrue('El nombre no debe tener mas de 25 caracteres' in str(context.exception))

    def test_minlen_3(self):
        ahorcado = Ahorcado()
        with self.assertRaises(Exception) as context:    
            ahorcado.login('xd')
        self.assertTrue('El nombre debe tener mas de 2 caracteres' in str(context.exception))
    def test_caracteres_especiales(self):
        ahorcado = Ahorcado()
        with self.assertRaises(Exception) as context:    
            ahorcado.login('@3hola')
        self.assertTrue('El nombre no puede tener caracteres especiales o espacios' in str(context.exception))
    def test_espacios_vacios(self):
        ahorcado = Ahorcado()
        with self.assertRaises(Exception) as context:    
            ahorcado.login('Agustin Etcheverry')
        self.assertTrue('El nombre no puede tener caracteres especiales o espacios' in str(context.exception))
    def test_getName(self):
        ahorcado = Ahorcado()
        ahorcado.login('Agustin')
        self.assertEqual('Agustin',ahorcado.get_name())

class TestJuego(unittest.TestCase):
    def test_inicializarVariables(self):
        ahorcado = Ahorcado()
        ahorcado.inicializarJuego()
        self.assertEqual(ahorcado.get_vidas(),7)
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
            self.assertEqual(ahorcado.get_vidas(),6)



if __name__ == '__main__':
    unittest.main()