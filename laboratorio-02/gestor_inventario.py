
CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

productos = []

opcion = ""

while opcion != "0":
    print()
    print("================================")
    print("      GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        codigo_repetido = False
        for producto in productos:
            if producto["codigo"] == codigo:
                codigo_repetido = True
                break

        if codigo == "" or nombre == "" or categoria == "":
            print("El código, el nombre y la categoría no pueden estar vacíos.")
        elif codigo_repetido:
            print("Ya existe un producto con ese código.")
        elif categoria not in CATEGORIAS:
            print("Categoría no permitida. Opciones:", ", ".join(CATEGORIAS))
        elif precio <= 0:
            print("El precio debe ser mayor que cero.")
        elif cantidad < 0:
            print("La cantidad no puede ser negativa.")
        else:
            nuevo_producto = {
                "codigo": codigo,
                "nombre": nombre,
                "categoria": categoria,
                "precio": precio,
                "cantidad": cantidad
            }
            productos.append(nuevo_producto)
            print("Producto registrado.")

    elif opcion == "2":
        if len(productos) == 0:
            print("El inventario está vacío: no hay registros.")
        else:
            for producto in productos:
                print(f"{producto['codigo']} - {producto['nombre']} - "
                      f"{producto['categoria']} - ${producto['precio']} - "
                      f"{producto['cantidad']} unidades")

    elif opcion == "3":
        codigo_buscado = input("Código a buscar: ").strip()

        encontrado = None
        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            print("Código:", encontrado["codigo"])
            print("Nombre:", encontrado["nombre"])
            print("Categoría:", encontrado["categoria"])
            print("Precio: $", encontrado["precio"])
            print("Cantidad:", encontrado["cantidad"])
        else:
            print("El producto no existe.")

    elif opcion == "4":
        codigo_buscado = input("Código del producto: ").strip()

        encontrado = None
        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")
        else:
            nueva_cantidad = int(input("Nueva cantidad disponible: "))
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa. Se conserva la anterior.")
            else:
                encontrado["cantidad"] = nueva_cantidad
                print("Existencias actualizadas.")

    elif opcion == "5":
        codigo_buscado = input("Código del producto a eliminar: ").strip()

        encontrado = None
        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")
        else:
            productos.remove(encontrado)
            print("Producto eliminado.")

    elif opcion == "6":
        agotados = [
            producto["nombre"] for producto in productos if producto["cantidad"] == 0
        ]
        if len(agotados) == 0:
            print("No hay productos sin existencias.")
        else:
            print("Sin existencias:")
            for nombre in agotados:
                print("-", nombre)

    elif opcion == "7":
        cantidad_productos = len(productos)
        unidades_totales = sum([producto["cantidad"] for producto in productos])
        valor_inventario = sum(
            [producto["precio"] * producto["cantidad"] for producto in productos],
            0.0
        )
        categorias_utilizadas = {producto["categoria"] for producto in productos}

        print("Productos:", cantidad_productos)
        print("Unidades:", unidades_totales)
        print("Valor del inventario: $", valor_inventario)
        if len(categorias_utilizadas) == 0:
            print("Categorías utilizadas: ninguna")
        else:
            print("Categorías utilizadas:", ", ".join(sorted(categorias_utilizadas)))

    elif opcion == "0":
        print("Programa finalizado.")

    else:
        print("Opción no válida.")

