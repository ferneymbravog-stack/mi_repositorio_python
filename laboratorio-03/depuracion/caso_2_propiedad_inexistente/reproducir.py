from inventario import Inventario
from producto import Producto

inventario = Inventario()
inventario.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
print(inventario.productos_sin_stock())
