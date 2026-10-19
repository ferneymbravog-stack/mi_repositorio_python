import json
from pathlib import Path

ruta = Path("libros.json")

libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "El coronel no tiene quien le escriba", "autor": "Gabriel García Márquez", "anio": 1961},
    {"codigo": "L003", "titulo": "Rayuela", "autor": "Julio Cortázar", "anio": 1963}
]

with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(libros, archivo, ensure_ascii=False, indent=4)

with ruta.open("r", encoding="utf-8") as archivo:
    guardados = json.load(archivo)

for libro in guardados:
    print(libro["codigo"], "-", libro["titulo"], "-", libro["autor"], "-", libro["anio"])

