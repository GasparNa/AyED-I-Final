# Ejercicio 8
'''
Crea una clase llamada Cubo, y asígnale el atributo de clase:
    caras = 6
y el atributo de instancia:
    color
Crea una instancia cubo_rojo, de dicho color.
'''
class Cubo: # Se crea la clase
    caras = 6 # Asigna un atributo
    def __init__(self, color): # Se crea la clase
        self.color = color

cubo_rojo = Cubo("rojo")

# --- Prueba ---
print(f"El cubo es de color {cubo_rojo.color}")