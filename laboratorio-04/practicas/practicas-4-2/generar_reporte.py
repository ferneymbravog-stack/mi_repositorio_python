from pathlib import Path

carpeta = Path(__file__).resolve().parent / "reportes"
carpeta.mkdir(parents=True, exist_ok=True)

ruta = carpeta / "resumen.txt"
ruta.write_text(
    "Productos registrados: 3\nUnidades disponibles: 6\nValor total: 1740000\n",
    encoding="utf-8",
)

print(ruta.read_text(encoding="utf-8"))
print("Guardado en:", ruta)

