
cantidad = int(input("Cantidad de notas: "))

if cantidad > 0:
    suma = 0.0

    for numero_nota in range(1, cantidad + 1):
        nota = float(input(f"Nota {numero_nota}: "))
        suma += nota

    promedio = suma / cantidad
    print("Promedio:", promedio)
else:
    print("La cantidad de notas debe ser mayor que cero.")

