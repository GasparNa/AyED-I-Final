# Ejercicio 07
'''
"El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)
Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:
    - poner_huevos()
    - tiene_pico = True
    - vertebrado = True
    - venenoso = True
    - nadar()
    - caminar()
    - amamantar()
'''
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero): # Herencia multiple
    pass # No se requiere nada nuevo


orni1 = Ornitorrinco() ##
'''
print(f'Orni\
      \nesta {orni1.poner_huevos()}\
      \ntiene pico:{orni1.tiene_pico}\
      \nes vertebrado: {orni1.vertebrado}\
      \nes venenoso: {orni1.venenoso}\
      \nnadando: {orni1.nadar()}\
      \ncaminando: {orni1.caminar()}\
      \namamantando: {orni1.amamantar()}')
'''
orni1.poner_huevos() # Hereda de  Ave
print(f'Tiene Pico? {orni1.tiene_pico}') #Hereda de Ave
print(f'Es vertebrado? {orni1.vertebrado}') # hereda de vertebrado
print(f'Es venenoso? {orni1.venenoso}') # Hereda de reptil
orni1.nadar() # Hereda de pez
orni1.caminar() # Hereda de mamifero
orni1.amamantar() # Hereda de mamifero