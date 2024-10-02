"""SUMA DE NÚMEROS PARES
Imagina que tienes una lista de números y quieres saber cuánto suman solo los números pares. Por ejemplo, si tienes los números del 1 al 10, queremos sumar 2 + 4 + 6 + 8 + 10.
Tu tarea es escribir una función que:
1. Reciba una lista de números.
2. Recorra esa lista y sume solo los números pares.
3. Devuelva el resultado de esa suma.
Ejemplo:
- Si la lista es [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- La función debe devolver 30 (que es 2 + 4 + 6 + 8 + 10)
Nota: Recuerda que puedes saber si un número es par si al dividirlo por 2 no tiene residuo."""

def suma_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = suma_pares(numeros)
print(f"La suma de los números pares es: {resultado}")