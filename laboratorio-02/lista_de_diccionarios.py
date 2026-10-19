
productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 7},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

for producto in productos:
    print(producto["codigo"], "-", producto["nombre"])

valor_inventario = 0
for producto in productos:
    valor_inventario += producto["precio"] * producto["cantidad"]
print("Valor del inventario:", valor_inventario)

codigo_buscado = input("Código: ").strip()
encontrado = False

for producto in productos:
    if producto["codigo"] == codigo_buscado:
        print("Encontrado:", producto["nombre"])
        encontrado = True
        break

if not encontrado:
    print("No se encontró el producto.")

