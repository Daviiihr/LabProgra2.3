# Longitud de cada palabra usando map()

palabras = ["uno", "dos", "tres"]
longitudes = list(map(len, palabras))  # también podría ser lambda x: len(x)
print(longitudes)
