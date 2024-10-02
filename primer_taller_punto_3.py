"""INVERTIR UNA LISTA
Imagina que tienes una lista de elementos y quieres crear una nueva lista con los mismos elementos, pero en orden inverso, como si la lista original se reflejara en un espejo.
Tu tarea es escribir una función que:
1. Reciba una lista de elementos.
2. Cree una nueva lista con los mismos elementos, pero en orden inverso.
3. Devuelva esta nueva lista invertida.
Ejemplo:
- Si la lista original es [1, 2, 3, 4, 5]
- La nueva lista invertida debe ser [5, 4, 3, 2, 1]
Nota: Piensa en cómo podrías recorrer la lista original desde el último elemento hasta el primero.
Recuerda:
- No modifiques la lista original en ninguno de estos ejercicios.
- Crea nuevas listas para almacenar los resultados.
- Prueba tus funciones con diferentes ejemplos para asegurarte de que funcionan correctamente.
- Si te atascas, no dudes en pedir ayuda o buscar recursos adicionales."""

def invertir_lista(lista_original):
    lista_invertida = []
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])
    return lista_invertida

# Ejemplo de uso
lista_original = [1, 2, 3, 4, 5]
resultado = invertir_lista(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista invertida: {resultado}")