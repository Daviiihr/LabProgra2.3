# Iterador que recorre una lista de cadenas y devuelve cada una en mayúsculas

class MayusIterator:
    # Iterador que recorre una lista de cadenas y devuelve cada una en mayúsculas.
    def __init__(self, cadenas):
        self.cadenas = cadenas
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.cadenas):
            raise StopIteration
        cadena = self.cadenas[self.indice].upper()
        self.indice += 1
        return cadena


if __name__ == "__main__":
    lista = ["python", "java", "c++", "ruby"]
    for texto in MayusIterator(lista):
        print(texto)
