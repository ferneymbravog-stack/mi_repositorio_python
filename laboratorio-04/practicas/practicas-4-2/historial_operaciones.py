from pathlib import Path

RUTA = Path(__file__).resolve().parent / "operaciones.txt"


def registrar():
    concepto = input("Concepto: ").strip()
    if concepto == "":
        print("El concepto es obligatorio.")
        return
    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("El valor debe ser numérico.")
        return
    with open(RUTA, "a", encoding="utf-8") as archivo:
        archivo.write(f"{concepto};{valor}\n")
    print("Operación registrada.")


def mostrar():
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("Todavía no hay operaciones registradas.")
        return
    if not lineas:
        print("El historial está vacío.")
        return
    for numero, linea in enumerate(lineas, start=1):
        concepto, valor = linea.strip().split(";")
        print(f"{numero}. {concepto} - {valor}")


while True:
    print("\n1. Registrar operación")
    print("2. Mostrar historial")
    print("0. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        registrar()
    elif opcion == "2":
        mostrar()
    elif opcion == "0":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")

