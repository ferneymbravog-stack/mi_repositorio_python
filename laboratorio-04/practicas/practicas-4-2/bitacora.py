nombre = input("Nombre de la prueba: ")

while True:
    resultado = input("Resultado (aprobada/fallida): ").strip().lower()
    if resultado in ("aprobada", "fallida"):
        break
    print("Escribe aprobada o fallida.")

observacion = input("Observación breve: ")

with open("pruebas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre} | {resultado} | {observacion}\n")

print("Registro agregado.")

