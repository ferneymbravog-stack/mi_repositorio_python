
productos = ["Teclado", "Mouse", "Monitor"]

buscado = input("Buscar producto: ").strip()

if buscado in productos:
    print("Producto encontrado.")
else:
    print("Producto no registrado.")

nombre = input("Producto a eliminar: ").strip()

if nombre in productos:
    productos.remove(nombre)
    print("Producto eliminado.")
else:
    print("No se encontró el producto.")

print(productos)

