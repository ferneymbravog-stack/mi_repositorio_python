from inventario import Inventario
from producto import Producto


def crear(codigo, nombre, categoria, precio, cantidad):
    try:
        return Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print("  rechazado:", error)
        return None


inventario = Inventario()

print("Inventario vacío:", inventario.listar_productos(), inventario.resumen())

print("Registrar P001:", inventario.registrar_producto(
    Producto("P001", "Teclado", "Periféricos", 85000, 4)))
print("Registrar P001 otra vez:", inventario.registrar_producto(
    Producto("P001", "Otro", "Periféricos", 1000, 1)))

print("Código vacío:", crear("  ", "X", "Periféricos", 10, 1))
print("Nombre vacío:", crear("P9", "  ", "Periféricos", 10, 1))
print("Categoría inválida:", crear("P9", "X", "Ropa", 10, 1))
print("Precio cero:", crear("P9", "X", "Periféricos", 0, 1))
print("Precio negativo:", crear("P9", "X", "Periféricos", -5, 1))
print("Cantidad negativa:", crear("P9", "X", "Periféricos", 10, -1))

print("Cantidad cero válida:", inventario.registrar_producto(
    Producto("P002", "Mouse", "Periféricos", 45000, 0)))
print("Registrar P003:", inventario.registrar_producto(
    Producto("P003", "Procesador", "Componentes", 700000, 2)))

encontrado = inventario.buscar_por_codigo("P001")
print("Buscar P001:", encontrado.nombre if encontrado else None)
print("Buscar P999:", inventario.buscar_por_codigo("P999"))

print("Actualizar P001 a 10:", inventario.actualizar_existencias("P001", 10))
print("Cantidad P001:", inventario.buscar_por_codigo("P001").cantidad)
print("Actualizar P001 a -3:", inventario.actualizar_existencias("P001", -3))
print("Cantidad P001:", inventario.buscar_por_codigo("P001").cantidad)

print("Eliminar P001:", inventario.eliminar_producto("P001"))
print("Eliminar P999:", inventario.eliminar_producto("P999"))

inventario.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
print("Resumen:", inventario.resumen())
print("Sin stock:", inventario.productos_sin_stock())
inventario.actualizar_existencias("P002", 5)
print("Tras actualizar P002:", inventario.resumen())

