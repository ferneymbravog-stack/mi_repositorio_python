# ==============================================================
# PLAN DE CÁLCULOS (Orden de operaciones):
# 1. Calcular el subtotal: precio unitario * cantidad.
# 2. Calcular el valor del descuento: subtotal * (porcentaje_descuento / 100).
# 3. Calcular la base gravable: subtotal - valor del descuento.
# 4. Calcular el valor del impuesto: base * (porcentaje_impuesto / 100).
# 5. Calcular el total final: base + valor del impuesto.
# ==============================================================

# Encabezado
print("=============================")
print("      COTIZADOR PYTHON       ")
print("=============================")
print()

# 1. Entrada de datos por el usuario
nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento (%): "))
porcentaje_impuesto = float(input("Impuesto (%): "))

# 2. Cálculos paso a paso (cada valor almacenado en su variable)
subtotal = precio_unitario * cantidad
valor_descuento = subtotal * (porcentaje_descuento / 100)
base = subtotal - valor_descuento
valor_impuesto = base * (porcentaje_impuesto / 100)
total = base + valor_impuesto

# 3. Resumen ordenado de compra
print()
print("-----------------------------")
print("RESUMEN DE COMPRA")
print("-----------------------------")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"TOTAL: ${total}")

