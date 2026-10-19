from producto import Producto, CATEGORIAS
from inventario import Inventario


def mostrar_menu():
    print()
    print("================================")
    print(" GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Buscar por categoría")
    print("9. Listar ordenado por nombre")
    print("10. Actualizar precio")
    print("11. Reporte completo")
    print("0. Salir")


def leer_cantidad(mensaje="Cantidad: "):
    while True:
        try:
            cantidad = int(input(mensaje))
        except ValueError:
            print("Debes escribir un número entero.")
            continue
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue
        return cantidad


def leer_precio(mensaje="Precio: "):
    while True:
        try:
            precio = float(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido.")
            continue
        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue
        return precio


def mostrar_producto(producto):
    print(
        f"{producto.codigo} - {producto.nombre} - {producto.categoria} - "
        f"${float(producto.precio)} - {producto.cantidad} unidades"
    )


def registrar(inventario):
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    print("Categorías:", ", ".join(CATEGORIAS))
    categoria = input("Categoría: ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()
    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print("No se registró el producto:", error)
        return
    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print("Ya existe un producto con ese código.")


def listar(inventario):
    productos = inventario.listar_productos()
    if not productos:
        print("El inventario está vacío.")
        return
    for producto in productos:
        mostrar_producto(producto)


def buscar(inventario):
    codigo = input("Código: ").strip()
    producto = inventario.buscar_por_codigo(codigo)
    if producto is None:
        print("Producto no registrado.")
    else:
        mostrar_producto(producto)


def actualizar(inventario):
    codigo = input("Código: ").strip()
    if inventario.buscar_por_codigo(codigo) is None:
        print("Producto no registrado.")
        return
    nueva_cantidad = leer_cantidad("Nueva cantidad: ")
    if inventario.actualizar_existencias(codigo, nueva_cantidad):
        print("Existencias actualizadas.")
    else:
        print("No se pudo actualizar.")


def eliminar(inventario):
    codigo = input("Código: ").strip()
    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no registrado.")


def mostrar_sin_stock(inventario):
    agotados = inventario.productos_sin_stock()
    if not agotados:
        print("No hay productos sin existencias.")
        return
    print("Sin existencias:")
    for nombre in agotados:
        print("-", nombre)


def mostrar_resumen(inventario):
    datos = inventario.resumen()
    categorias = ", ".join(sorted(datos["categorias"])) or "Ninguna"
    print("Productos registrados:", datos["productos"])
    print("Unidades disponibles:", datos["unidades"])
    print(f"Valor del inventario: ${float(datos['valor'])}")
    print("Categorías utilizadas:", categorias)


def buscar_categoria(inventario):
    print("Categorías:", ", ".join(CATEGORIAS))
    categoria = input("Categoría: ").strip()
    productos = inventario.buscar_por_categoria(categoria)
    if not productos:
        print("No hay productos en esa categoría.")
        return
    for producto in productos:
        mostrar_producto(producto)


def listar_ordenados(inventario):
    productos = inventario.listar_ordenados_por_nombre()
    if not productos:
        print("El inventario está vacío.")
        return
    for producto in productos:
        mostrar_producto(producto)


def actualizar_precio(inventario):
    codigo = input("Código: ").strip()
    if inventario.buscar_por_codigo(codigo) is None:
        print("Producto no registrado.")
        return
    nuevo_precio = leer_precio("Nuevo precio: ")
    if inventario.actualizar_precio(codigo, nuevo_precio):
        print("Precio actualizado.")
    else:
        print("No se pudo actualizar el precio.")


def mostrar_reporte(inventario):
    print("----- REPORTE DEL INVENTARIO -----")
    mostrar_resumen(inventario)

    mayor = inventario.producto_mayor_valor()
    if mayor is None:
        print("Producto de mayor valor: ninguno")
    else:
        print(
            f"Producto de mayor valor: {mayor.nombre} "
            f"(${float(mayor.calcular_valor())})"
        )

    nombres = inventario.nombres_por_codigo()
    print("Códigos registrados:")
    for codigo, nombre in nombres.items():
        print(f"  {codigo} -> {nombre}")


def main():
    inventario = Inventario()
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()
        if opcion == "1":
            registrar(inventario)
        elif opcion == "2":
            listar(inventario)
        elif opcion == "3":
            buscar(inventario)
        elif opcion == "4":
            actualizar(inventario)
        elif opcion == "5":
            eliminar(inventario)
        elif opcion == "6":
            mostrar_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "8":
            buscar_categoria(inventario)
        elif opcion == "9":
            listar_ordenados(inventario)
        elif opcion == "10":
            actualizar_precio(inventario)
        elif opcion == "11":
            mostrar_reporte(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

