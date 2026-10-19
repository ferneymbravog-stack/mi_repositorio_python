import json
from pathlib import Path

ruta = Path("productos.json")
productos = []
archivo_danado = False

try:
    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
except FileNotFoundError:
    print("El archivo no existe. Se inicia con una lista vacía.")
except json.JSONDecodeError as error:
    archivo_danado = True
    print("El archivo no contiene JSON válido:", error)
else:
    print("Productos cargados:", len(productos))

if archivo_danado:
    print("No se guardará nada sobre el archivo. Revisa su contenido:")
    print(ruta.read_text(encoding="utf-8"))
else:
    productos.append({"codigo": "P099", "nombre": "Cable", "precio": 5000, "cantidad": 10})
    with ruta.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)
    print("Archivo guardado.")

