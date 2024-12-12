# Esjercicio 01
'''
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
Si la suma es menor o igual a 6:
    "La suma de tus dados es {suma_dados}. Lamentable"
Si la suma es mayor a 6 y menor a 10:
    "La suma de tus dados es {suma_dados}. Tienes buenas chances"
Si la suma es mayor o igual a 10:
    "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6
'''
from random import * # imporamos la biblioteca

def lanzar_dados(): # Creamos la Fn
    dado1 = randint(1,6) # Asignamos valor al dado1
    dado2 = randint(1,6) # Asignamos valor al dado2
    return dado1, dado2 # Retornamos los resultados

def evaluar_jugada(dado1, dado2): # Creamos la Fn
    suma = dado1 + dado2 # Sumamos los valores
    if suma <= 6: # Comprobación
        print(f'La suma de tus dados es {suma}. Lamentable')
    elif suma > 6 and suma < 10: # Comprobación
        print(f'La suma de tus dados es {suma}. Tienes buenas chances')
    else: # Comprobación
        print(f'La suma de tus dados es {suma}. Parece una jugada ganadora')

# --- Pruebas ---
dados = lanzar_dados()
evaluar_jugada(dados[0], dados[1])