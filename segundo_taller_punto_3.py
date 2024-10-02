"""Escribe un programa que lea una lista de palabras e imprima la lista de palabras que comiencen con una determinada letra."""

def filtrar_palabras_por_letra(lista_palabras, letra):
    letra = letra.lower()
    return [palabra for palabra in lista_palabras if palabra.lower().startswith(letra)]

palabras = input("Ingresa una lista de palabras separadas por espacios: ").split()

letra = input("Ingresa la letra para filtrar las palabras: ")

palabras_filtradas = filtrar_palabras_por_letra(palabras, letra)
print("Palabras que comienzan con la letra '{}':".format(letra))
print(palabras_filtradas)