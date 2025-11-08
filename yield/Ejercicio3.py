# Clase con __iter__ que usa yield para cuadrados del 1 al 10

class Cuadrados:
    # Genera los cuadrados de los números del 1 al 10 usando yield en __iter__.
    def __iter__(self):
        for i in range(1, 11):
            yield i ** 2


if __name__ == "__main__":
    for c in Cuadrados():
        print(c)
