# Ejercicio 06

'''
Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"
# [1]: asegúrate de utilizar return seguido de una cadena de texto
'''
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre): # Creación de la clase hijo
    def hobby(self): # reescritura de la Fn 
        return "Juego videojuegos en mi tiempo libre" # Nuevo valor
    
# --- Pruebas ---
juan = Hijo()
print(f'Juan heredo de su padre los ojos {juan.color_ojos}, su pelo {juan.tipo_pelo}, su altura {juan.altura}, su voz {juan.voz},\
      \nle gusta el mismo deporte {juan.deporte_preferido}, su forma de reir {juan.reir()}, en su andar {juan.caminar()}, eso ¡sí! el hobby NO, el prefiere  {juan.hobby()}')