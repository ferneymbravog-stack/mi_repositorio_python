
productos = ["Teclado", "Mouse", "Monitor"]
print(productos)
print(type(productos))

print(productos[0])
print(productos[1])
print(productos[2])
print(productos[-1])

otros = []
otros.append("Teclado")
otros.append("Mouse")
otros.append("Monitor")
print(otros)
print("Cantidad:", len(otros))

nuevo_producto = input("Producto nuevo: ").strip()
otros.append(nuevo_producto)
print(otros)

