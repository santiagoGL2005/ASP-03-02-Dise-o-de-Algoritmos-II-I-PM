"""
Aplicación de la estructura FOR
1. Pide al usuario que ingrese una palabra o frase y usa un ciclo for para contar cuántas vocales (a, e, i, o, u) contiene. Luego, muestra el conteo de cada vocal por separado."""

texto = input("Por favor, ingresa una palabra o frase: ")

texto = texto.lower()

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in texto:
    if letra in vocales:
        vocales[letra] += 1

print("\nConteo de vocales:")
for vocal, conteo in vocales.items():
    print(f"{vocal}: {conteo}")

total_vocales = sum(vocales.values())
print(f"\nTotal de vocales: {total_vocales}")