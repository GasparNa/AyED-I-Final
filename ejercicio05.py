# Ejercicio 05
'''# 
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
    real = False
Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
    especie = "Humano"
    magico = True
    edad = 17
'''
class Personaje: # Creacion de la clase
    real = False # Atributo

class HarryPotter(Personaje): # Creacion de clase hija de Personaje
    especie = "Humano" # Atributo
    magico = True # Atributo
    edad = 17 # Atributo


# --- Pruebas ---
harry_potter = HarryPotter()
print(harry_potter.real)
print(harry_potter.especie)
print(harry_potter.magico)
print(harry_potter.edad)