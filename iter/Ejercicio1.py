# Contador del 10 al 15 usando iter() y next()

numeros = range(10, 16)
iterador = iter(numeros)

if __name__ == "__main__":
    while True:
        try:
            print(next(iterador))
        except StopIteration:
            break
