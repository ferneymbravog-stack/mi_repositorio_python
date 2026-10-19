
productos = ["Teclado", "Mouse", "Monitor"]
nuevos = ["Impresora", "Cámara"]
print("Inicial:", productos)

posicion = productos.index("Mouse")
productos[posicion] = "Mouse inalámbrico"
print("1. Reemplazo:", productos)

productos.insert(0, "Parlantes")
print("2. Inserción:", productos)

productos.extend(nuevos)
print("3. Extend:", productos)

productos.remove("Monitor")
print("4. Remove:", productos)

ultimo = productos.pop()
print("5. Pop:", productos)
print("Elemento extraído:", ultimo)


