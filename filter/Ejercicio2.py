# Filtrar palabras que empiezan con "p"

palabras = ["perro", "gato", "pato", "hamster"]
empiezan_con_p = list(filter(lambda x: x.startswith("p"), palabras))
print(empiezan_con_p)
