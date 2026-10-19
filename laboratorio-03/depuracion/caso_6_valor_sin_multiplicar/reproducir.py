from inventario import Inventario
from producto import Producto

inventario = Inventario()
inventario.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
inventario.registrar_producto(Producto("P002", "Mouse", "Periféricos", 45000, 0))
inventario.registrar_producto(Producto("P003", "Procesador", "Componentes", 700000, 2))
print("Valor del inventario (esperado 1740000):", inventario.resumen()["valor"])
