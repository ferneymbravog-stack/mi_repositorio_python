
total_ahorrado = 0
depositos_validos = 0

deposito = int(input("Depósito (0 para terminar): "))

while deposito != 0:
    if deposito > 0:
        total_ahorrado += deposito
        depositos_validos += 1
        print("Ahorro acumulado:", total_ahorrado)
    else:
        print("El depósito debe ser positivo.")

    deposito = int(input("Depósito (0 para terminar): "))

print("Depósitos válidos:", depositos_validos)
print("Total ahorrado:", total_ahorrado)

