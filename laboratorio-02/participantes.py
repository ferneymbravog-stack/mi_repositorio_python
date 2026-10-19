
lista_manana = ["Ana", "Luis", "Ana", "Camila"]
lista_tarde = ["Luis", "Pedro", "Camila", "Pedro"]

participantes = set(lista_manana + lista_tarde)
print("Personas diferentes:", len(participantes))
print(participantes)

participantes.add("Sofía")
print("Tras add('Sofía'):", participantes)

participantes.discard("Pedro")
print("Tras discard('Pedro'):", participantes)
print("Personas diferentes ahora:", len(participantes))

