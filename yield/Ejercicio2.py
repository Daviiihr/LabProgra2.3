# Generador que recibe una lista y devuelve solo los impares

def filtrar_impares(numeros):
    # Recibe una lista de números y va devolviendo solo los impares.
    for n in numeros:
        if n % 2 != 0:
            yield n


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for impar in filtrar_impares(lista):
        print(impar)
