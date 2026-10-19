
productos = ["Teclado", "Mouse", "Monitor", "Cámara", "Parlantes"]
print(productos[0:2])
print(productos[2:])
print(productos[:3])
print(productos[-2:])

desordenados = ["Monitor", "Cámara", "Teclado"]
ordenados = sorted(desordenados)
print("Original:", desordenados)
print("Ordenados:", ordenados)
desordenados.sort()
print("Tras sort():", desordenados)

original = ["Teclado", "Mouse"]
otra_referencia = original
otra_referencia.append("Monitor")
print(original)

original = ["Teclado", "Mouse"]
copia = original.copy()
copia.append("Monitor")
print("Original:", original)
print("Copia:", copia)

