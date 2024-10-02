"""Escribe un programa lea una lista de números e imprima la suma de los números pares."""

def suma_pares(numeros):
    return sum(num for num in numeros if num % 2 == 0)

entrada = input("Ingrese una lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

resultado = suma_pares(numeros)

print(f"La suma de los números pares es: {resultado}")