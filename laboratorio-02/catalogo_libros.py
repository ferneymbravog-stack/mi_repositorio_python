
libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "El coronel no tiene quien le escriba", "autor": "Gabriel García Márquez", "anio": 1961},
    {"codigo": "L003", "titulo": "Rayuela", "autor": "Julio Cortázar", "anio": 1963}
]

codigo_buscado = input("Código del libro a consultar: ").strip()
encontrado = None

for libro in libros:
    if libro["codigo"] == codigo_buscado:
        encontrado = libro
        break

if encontrado is not None:
    print("Título:", encontrado["titulo"])
    print("Autor:", encontrado["autor"])
    print("Año:", encontrado["anio"])
else:
    print("El libro no fue localizado.")

print()
print("Registrar un libro nuevo")
codigo = input("Código: ").strip()

codigo_repetido = False
for libro in libros:
    if libro["codigo"] == codigo:
        codigo_repetido = True
        break

if codigo == "":
    print("El código no puede estar vacío.")
elif codigo_repetido:
    print("Ya existe un libro con ese código.")
else:
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = int(input("Año: "))
    libros.append({"codigo": codigo, "titulo": titulo, "autor": autor, "anio": anio})
    print("Libro registrado.")

print("Libros registrados:", len(libros))

