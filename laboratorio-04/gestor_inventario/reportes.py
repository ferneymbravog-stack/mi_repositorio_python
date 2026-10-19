import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"

CAMPOS = ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"]


def exportar_csv(inventario):
    filas = []
    for dato in inventario.exportar_datos():
        fila = dict(dato)
        fila["valor_inventario"] = dato["precio"] * dato["cantidad"]
        filas.append(fila)
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)
    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(filas)
    return RUTA_CSV

