# Ejercicio 02
'''
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
'''
from random import * # importamos la biblioteca

def lanzar_moneda(): # Se crea la Fn
    moneda = choice(['Cara', 'Cruz']) # Se lanza la moneda
    return moneda # Se devuelve el valor de moneda

def probar_suerte(moneda, lista_numeros): # Se crea la Fn
    if moneda == 'Cara': # Comprobación
        print('La lista se autodestruirá') # Imprime el mensaje
        return [] # Devuelve la lista vacia
    else: # Comprobación
        print('La lista fue salvada') # Imprime el mensaje
        return lista_numeros # Devuelve la lista
    
# --- Pruebas ---
moneda = lanzar_moneda() # Ejecución de la Fn
print(probar_suerte(moneda, [1,2,3,4,5])) 