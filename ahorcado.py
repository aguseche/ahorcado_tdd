from utils import validaciones_nombre
import random
import os

class Ahorcado:
    name:str
    palabra: str     
    palabras=["caramelo","auto","salir","pato","puerta"]   
    palabra:str  
    
    # constructor

    def __init__(self):
        self.name = None
        
    # gets

    def get_name(self)->str:
        return self.name
    
    def get_vidas(self)->int:
        return  self.vidas

    # methods
    def inicializarJuego(self):        
        self.resultado = []
        self.letras_erroneas = []
        self.vidas=7
        self.palabra = list(random.choice(self.palabras))
        for l in range(len(self.palabra)):
            self.resultado.append("_")

    def restar_vida(self)->int:
        self.vidas-=1

    def login(self,name)-> None:
        validaciones_nombre(name)
        self.name = name
    
    def prueba_letra(self, letra:str)-> bool:
        if letra in self.palabra:
            return True
        return False

    def agregar_letra(self, letra:str)-> None:
        if self.prueba_letra(letra=letra):                
            posiciones = []
            for pos,char in enumerate(self.palabra):
                if(char == letra):
                    posiciones.append(pos)
            for pos in posiciones:
                self.resultado[pos] = letra
        else:
            self.restar_vida()                
            self.letras_erroneas.append(letra)
        
      

    def validar_letra_repetida(self, letra:str)->bool:
        if (letra in self.resultado) or (letra in self.letras_erroneas):
            return False
        return True

    def validar_finalizacion(self)->bool:
        if(self.palabra==self.resultado):
            os.system("cls")
            print("/************************/ \n")  
            print("Ganasteee !!!! :) :D ")
            print("/************************/ \n")
            return True
        elif(self.vidas==0):   
            os.system("cls")
            print("/************************/ \n")         
            print("Perdiste :(")
            print("La palabra era: ","".join(self.palabra),"\n")
            print("/************************/ \n")
            return True
        else:
            return False

    def imprimirLetras(self,palab):
        for i in palab:
            print(i,end=" ")
        print("\n")

    def mostrarAhorcado(self):        
        print("/******AHORCADO******/")
        print("Palabra: ")
        self.imprimirLetras(self.resultado)
        print("Letras Incorrectas: ")
        self.imprimirLetras(self.letras_erroneas)
        print('Te quedan ',self.vidas,' vidas \n')
                        


    def jugar(self):
        print('Bienvenido al Ahorcado, ingrese su nombre: ')        
        name = input()            
        self.login(name)
        self.inicializarJuego()
        while True:
            while(not self.validar_finalizacion() ):
                os.system("cls")
                self.mostrarAhorcado()
                while True: 
                    print('ingrese una letra: (. para salir) ')
                    letraSF = input()
                    letra=letraSF.lower()                                  
                    if self.validar_letra_repetida(letra):  
                        self.agregar_letra(letra)    
                        break
                    else:
                        print("\n/************************/")
                        print('No puede repetir letras')
                        print("/************************/\n")
            print("Quiere jugar de nuevo? (s/n)")            
            resp=input()
            if(resp=="n"):
                break
            elif(resp=="s"):
                self.inicializarJuego()
                


if __name__ == '__main__':
    ahorcado = Ahorcado()
    ahorcado.jugar()

