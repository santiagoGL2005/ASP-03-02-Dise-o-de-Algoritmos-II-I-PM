"""Escribe un programa que lea una lista de nombres e imprima la lista en orden alfabético."""

def leer_nombres():
    nombres = []
    while True:
        nombre = input("Ingrese un nombre (o presione Enter para terminar): ")
        if nombre == "":
            break
        nombres.append(nombre)
    return nombres

def main():
    print("Organización de nombres.")

    lista_nombres = leer_nombres()

    lista_nombres.sort()

    print("\nLista de nombres en orden alfabético:")
    for nombre in lista_nombres:
        print(nombre)

if __name__ == "__main__":
    main()