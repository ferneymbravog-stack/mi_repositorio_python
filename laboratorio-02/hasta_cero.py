
numero = 1

while numero <= 5:
    print(numero)
    numero += 1

print("---")

cantidad_ingresados = 0

valor = int(input("Número: "))

while valor != 0:
    cantidad_ingresados += 1
    valor = int(input("Número: "))

print("Programa terminado.")
print("Números diferentes de cero ingresados:", cantidad_ingresados)

