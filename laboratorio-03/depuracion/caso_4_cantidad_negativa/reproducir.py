from producto import Producto

producto = Producto("P001", "Teclado", "Periféricos", 85000, -5)
print("Se creó un producto con cantidad:", producto.cantidad)
print("Valor del producto:", producto.calcular_valor())
