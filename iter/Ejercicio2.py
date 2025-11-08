# Clase con yield que genera impares del 1 al 20

class Impares:
    # Generador de números impares entre inicio y fin (por defecto 1 a 20).
    def __init__(self, inicio=1, fin=20):
        self.inicio = inicio
        self.fin = fin

    def __iter__(self):
        for i in range(self.inicio, self.fin + 1):
            if i % 2 != 0:
                yield i


if __name__ == "__main__":
    for numero in Impares():
        print(numero)
