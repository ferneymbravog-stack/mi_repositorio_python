import json
from pathlib import Path

from inventario import Inventario

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


class ErrorAlmacenamiento(Exception):
    pass


def guardar_inventario(inventario):
    datos = inventario.exportar_datos()
    try:
        RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)
        with RUTA_JSON.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
    except (OSError, TypeError) as error:
        raise ErrorAlmacenamiento(f"No se pudo guardar el inventario: {error}") from error
    return RUTA_JSON


def cargar_inventario():
    if not RUTA_JSON.exists():
        return Inventario()
    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except json.JSONDecodeError as error:
        raise ErrorAlmacenamiento(f"El archivo JSON tiene un formato incorrecto: {error}") from error
    except OSError as error:
        raise ErrorAlmacenamiento(f"No se pudo leer el archivo: {error}") from error
    try:
        return Inventario.desde_datos(datos)
    except ValueError as error:
        raise ErrorAlmacenamiento(f"El archivo contiene datos inválidos: {error}") from error

