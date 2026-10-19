
inscritos_python = {"Ana", "Carlos", "Laura", "Sara", "Mateo"}
inscritos_java = {"Laura", "Sara", "David", "Pablo"}

print("Al menos un taller:", inscritos_python | inscritos_java)
print("En ambos talleres:", inscritos_python & inscritos_java)
print("Solo Python:", inscritos_python - inscritos_java)
print("Solo Java:", inscritos_java - inscritos_python)
print("En uno solo de los talleres:", inscritos_python ^ inscritos_java)

