# Generar serie de Fibonacci hasta el décimo elemento

def fibonacci(n):
    # Genera n elementos de la serie de Fibonacci.
    
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    for numero in fibonacci(10):
        print(numero)
