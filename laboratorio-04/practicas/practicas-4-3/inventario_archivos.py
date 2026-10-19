import csv
import json
from pathlib import Path

RUTA_JSON = Path("inventario.json")
RUTA_CSV = Path("inventario.csv")


def guardar(productos):
    with RUTA_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)


def recuperar():
    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def exportar(productos):
    campos = ["codigo", "nombre", "precio", "cantidad"]
    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(productos)


try:
    productos = recuperar()
except json.JSONDecodeError:
    print("El archivo inventario.json tiene un formato inválido. No se modificará.")
else:
    print("Productos recuperados:", len(productos))
    codigo = f"P{len(productos) + 1:03d}"
    productos.append({"codigo": codigo, "nombre": "Producto " + codigo, "precio": 1000, "cantidad": 1})
    guardar(productos)
    exportar(productos)
    print("Inventario guardado y exportado. Total:", len(productos))

