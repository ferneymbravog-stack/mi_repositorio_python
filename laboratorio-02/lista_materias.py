
materias = ["Matemáticas", "Programación", "Bases de datos", "Inglés"]

for materia in materias:
    print("Materia:", materia)

print("---")

for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)

materias.append("Redes")
print("---")
for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)

