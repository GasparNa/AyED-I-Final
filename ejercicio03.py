# Ejercicio 03
'''
Ejercicio 3
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
'''
lista_numeros = [-5, -4, 8, 158, 687, 999, 1020]

def suma_menores(lista_numeros): # Crear la Fn
    suma = 0 # Crear la variable
    for i in range(len(lista_numeros)): # Crear la comprobación
        if lista_numeros[i] > 0 and lista_numeros[i] < 1000:
            suma += lista_numeros[i]
    return suma # Devuelve total de la suma

# --- Prueba ---
print(suma_menores(lista_numeros))
