# Concatenar todas las cadenas de una lista usando reduce()

from functools import reduce

cadenas = ["Hola", " ", "Mundo", "!"]
frase = reduce(lambda x, y: x + y, cadenas)
print(frase)
