"""ELIMINAR DUPLICADOS
A veces tenemos listas donde algunos elementos se repiten, pero queremos una lista donde cada elemento aparezca una sola vez.
Tu tarea es crear una función que:
1. Reciba una lista que puede tener elementos repetidos.
2. Cree una nueva lista que contenga los mismos elementos, pero sin repeticiones.
3. Mantenga el orden en que los elementos aparecieron por primera vez.
Ejemplo:
- Si la lista original es [1, 2, 2, 3, 4, 4, 5, 5, 6]
- La nueva lista debe ser [1, 2, 3, 4, 5, 6]
Nota: Puedes usar otra estructura de datos, como un conjunto (set), para ayudarte, pero recuerda que los conjuntos no mantienen el orden."""

def eliminar_duplicados(lista):
    elementos_vistos = set()
    resultado = []
    for elemento in lista:
        if elemento not in elementos_vistos:
            elementos_vistos.add(elemento)
            resultado.append(elemento)
    return resultado

lista_original = [1, 2, 2, 3, 4, 4, 5, 5, 6]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista sin dupllcados: {lista_sin_duplicados}")