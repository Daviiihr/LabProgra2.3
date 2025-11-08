# Lambda que recibe una lista y devuelve el primer elemento

primer_elemento = lambda lista: lista[0] if lista else None

if __name__ == "__main__":
    print(primer_elemento([1, 2, 3]))
    print(primer_elemento([]))  # None
