FACTOR_MILLAS = 0.621371

kilometros = float(input("Ingrese la distancia en kilómetros: "))

metros = kilometros * 1000
centimetros = kilometros * 100000
millas = kilometros * FACTOR_MILLAS

print("\n--- Conversión de Unidades ---")
print(f"Kilómetros  : {kilometros} km")
print(f"Metros      : {metros} m")
print(f"Centímetros : {centimetros} cm")
print(f"Millas      : {millas} millas")

