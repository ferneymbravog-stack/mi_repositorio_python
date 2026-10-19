import math

from almacenamiento import ErrorAlmacenamiento, cargar_inventario, guardar_inventario
from inventario import Inventario
from producto import CATEGORIAS, Producto
from reportes import exportar_csv

MENU = """
================================
GESTOR DE INVENTARIO
================================
1. Registrar producto
2. Listar productos
3. Buscar por código
4. Actualizar existencias
5. Eliminar producto
6. Consultar productos sin stock
7. Resumen del inventario
8. Guardar inventario
9. Exportar reporte CSV
0. Salir"""


def leer_precio():
    texto = input("Precio: ").strip()
    try:
        precio = float(texto)
    except ValueError:
        raise ValueError("El precio debe ser un número.")
    if not math.isfinite(precio):
        raise ValueError("El precio debe ser un número finito.")
    return precio


def leer_cantidad(mensaje="Cantidad: "):
    texto = input(mensaje).strip()
    try:
        return int(texto)
    except ValueError:
        raise ValueError("La cantidad debe ser un número entero.")


def intentar_guardar(inventario):
    try:
        guardar_inventario(inventario)
    except ErrorAlmacenamiento as error:
        print(error)
        print("Advertencia: los cambios podrían existir solamente en memoria.")
    else:
        print("Inventario guardado.")


def registrar(inventario):
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ")
    print("Categorías:", ", ".join(CATEGORIAS))
    categoria = input("Categoría: ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()
    producto = Producto(codigo, nombre, categoria, precio, cantidad)
    inventario.registrar(producto)
    print("Producto registrado.")
    return True


def listar(inventario):
    productos = inventario.listar()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(producto)


def buscar(inventario):
    codigo = input("Código: ").strip()
    producto = inventario.buscar(codigo)
    if producto is None:
        print("No existe un producto con ese código.")
    else:
        print(producto)


def actualizar(inventario):
    codigo = input("Código: ").strip()
    if inventario.buscar(codigo) is None:
        print("No existe un producto con ese código.")
        return False
    cantidad = leer_cantidad("Nueva cantidad: ")
    inventario.actualizar_existencias(codigo, cantidad)
    print("Existencias actualizadas.")
    return True


def eliminar(inventario):
    codigo = input("Código: ").strip()
    if inventario.buscar(codigo) is None:
        print("No existe un producto con ese código.")
        return False
    inventario.eliminar(codigo)
    print("Producto eliminado.")
    return True


def sin_stock(inventario):
    productos = inventario.sin_stock()
    if not productos:
        print("No hay productos sin existencias.")
        return
    for producto in productos:
        print(producto)


def resumen(inventario):
    print("Productos registrados:", inventario.total_productos())
    print("Unidades disponibles:", inventario.total_unidades())
    print("Valor total: $" + str(inventario.valor_total()))
    nombres = [producto.nombre for producto in inventario.sin_stock()]
    print("Sin existencias:", ", ".join(nombres) if nombres else "ninguno")
    print("Categorías utilizadas:", len(inventario.categorias_utilizadas()))


def exportar(inventario):
    try:
        ruta = exportar_csv(inventario)
    except OSError as error:
        print("No se pudo exportar el reporte:", error)
    else:
        print("Reporte exportado:", ruta)


def main():
    solo_lectura = False
    try:
        inventario = cargar_inventario()
    except ErrorAlmacenamiento as error:
        print(error)
        print("El archivo no será modificado. Las operaciones de cambio quedan bloqueadas.")
        inventario = Inventario()
        solo_lectura = True

    modificaciones = {"1": registrar, "4": actualizar, "5": eliminar}
    consultas = {"2": listar, "3": buscar, "6": sin_stock, "7": resumen, "9": exportar}

    while True:
        print(MENU)
        opcion = input("Opción: ").strip()
        if opcion == "0":
            print("Programa finalizado.")
            break
        if opcion in modificaciones:
            if solo_lectura:
                print("Operación bloqueada: el archivo de datos está dañado.")
                continue
            try:
                aceptada = modificaciones[opcion](inventario)
            except (ValueError, TypeError) as error:
                print("Operación rechazada:", error)
                continue
            if aceptada:
                intentar_guardar(inventario)
        elif opcion == "8":
            if solo_lectura:
                print("Operación bloqueada: el archivo de datos está dañado.")
            else:
                intentar_guardar(inventario)
        elif opcion in consultas:
            consultas[opcion](inventario)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

