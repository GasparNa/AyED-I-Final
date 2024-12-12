# Ejercicio 4
'''
Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.
Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate.
'''
def personaje_defender(personaje): # Se crea la Fn
    personaje.defender()

class Mago(): # Se crea la clase Mago
    def defender(self): # Instancia la clase Mago
        print("Escudo mágico") # Devolución

class Arquero(): # Se crea la clase Arquero
    def defender(self): # Instancia la clase
        print("Esconderse") # Devolución

class Samurai(): # Se crea la clase Samurai
    def defender(self): # Instancia la
        print("Bloqueo") # Devolución


# --- Pruebas ---
mago_gandalf = Mago() # Se crea un Mago
arquero_legolas = Arquero() # Se crea un Arquero
samurai_warrior = Samurai() # Se crea un Samurai

personaje_defender(mago_gandalf)
personaje_defender(arquero_legolas)
personaje_defender(samurai_warrior)