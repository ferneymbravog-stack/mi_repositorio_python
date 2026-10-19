from inventario import Inventario
from producto import Producto


def mostrar_resultado(descripcion, resultado):
    print(f"{descripcion}: {resultado}")


inventario = Inventario()

inventario.registrar_producto(Producto("P003", "Procesador", "Componentes", 700000, 2))
inventario.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
inventario.registrar_producto(Producto("P002", "Auriculares", "Accesorios", 45000, 0))
inventario.registrar_producto(Producto("P004", "Mouse", "Periféricos", 30000, 5))

print("--- Buscar por categoría: Periféricos ---")
for producto in inventario.buscar_por_categoria("Periféricos"):
    print(producto.codigo, producto.nombre)
mostrar_resultado("Categoría sin productos", inventario.buscar_por_categoria("Otra"))

print("--- Ordenados por nombre ---")
for producto in inventario.listar_ordenados_por_nombre():
    print(producto.nombre)

print("--- Actualizar precio ---")
mostrar_resultado("P001 a 90000", inventario.actualizar_precio("P001", 90000))
mostrar_resultado("Precio P001", inventario.buscar_por_codigo("P001").precio)
mostrar_resultado("P001 a -10", inventario.actualizar_precio("P001", -10))
mostrar_resultado("Precio P001 se conserva", inventario.buscar_por_codigo("P001").precio)
mostrar_resultado("P999 inexistente", inventario.actualizar_precio("P999", 1000))

print("--- Mayor valor ---")
mayor = inventario.producto_mayor_valor()
mostrar_resultado("Producto", mayor.nombre)
mostrar_resultado("Valor", mayor.calcular_valor())
mostrar_resultado("Inventario vacío", Inventario().producto_mayor_valor())

print("--- Código a nombre ---")
mostrar_resultado("Diccionario", inventario.nombres_por_codigo())

print("--- Independencia ---")
otro = Inventario()
mostrar_resultado("Otro inventario", len(otro.listar_productos()))

