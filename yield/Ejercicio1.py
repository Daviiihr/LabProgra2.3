# Generar los primeros 10 números pares usando yield

def generar_pares():
    # Genera los primeros 10 números pares: 2, 4, ..., 20.
    for i in range(1, 11):
        yield i * 2


if __name__ == "__main__":
    for numero in generar_pares():
        print(numero)
