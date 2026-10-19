
productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 7},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

codigo = input("Código del producto nuevo: ").strip()
nombre = input("Nombre: ").strip()
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

nuevo_producto = {
    "codigo": codigo,
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}
productos.append(nuevo_producto)

print()
for producto in productos:
    print(producto["codigo"], "-", producto["nombre"], "-", producto["precio"], "-", producto["cantidad"])

