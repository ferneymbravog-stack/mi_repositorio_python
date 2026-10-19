cantidad_compras = 0
acumulado = 0.0

while True:
    try:
        importe = float(input("Importe de la compra (0 para terminar): "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    if importe == 0:
        break
    if importe < 0:
        print("El importe debe ser positivo.")
        continue
    cantidad_compras += 1
    acumulado += importe

print("Compras aceptadas:", cantidad_compras)
print("Suma acumulada:", acumulado)

