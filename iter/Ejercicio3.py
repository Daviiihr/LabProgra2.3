# Clase que genera cuadrados del 1 al 10 sin usar iter()

class Cuadrados:
    # Devuelve una lista con los cuadrados de 1 a n (por defecto n = 10).

    def __init__(self, n=10):
        self.n = n

    def obtener_cuadrados(self):
        resultado = []
        for i in range(1, self.n + 1):
            resultado.append(i ** 2)
        return resultado


if __name__ == "__main__":
    c = Cuadrados()
    print(c.obtener_cuadrados())
