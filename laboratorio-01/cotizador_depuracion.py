# ==============================================================
# RETO DE DEPURACIÓN - ERRORES PROVOCADOS Y CORREGIDOS
# ==============================================================

# Encabezado
print("=============================")
print("  COTIZADOR - DEPURACIÓN     ")
print("=============================")
print()

nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento (%): "))
porcentaje_impuesto = float(input("Impuesto (%): "))

# --------------------------------------------------------------------------
# ERROR 1 (Sintaxis):
# ERROR ORIGINAL: subtotal = precio_unitario * (Faltaba el segundo operando o cerrar paréntesis)
# CORRECCIÓN: Se completó la expresión multiplicando precio_unitario por cantidad.
# --------------------------------------------------------------------------
subtotal = precio_unitario * cantidad

# --------------------------------------------------------------------------
# ERROR 2 (Nombre de variable inexistente - NameError):
# ERROR ORIGINAL: valor_descuento = sub_total * (porcentaje_descuento / 100) -> 'sub_total' no existe, está definida como 'subtotal'.
# CORRECCIÓN: Se corrigió el nombre de la variable a 'subtotal'.
# --------------------------------------------------------------------------
valor_descuento = subtotal * (porcentaje_descuento / 100)

base = subtotal - valor_descuento

valor_impuesto = base * (porcentaje_impuesto / 100)

# --------------------------------------------------------------------------
# ERROR 3 (Error lógico / cálculo incorrecto):
# ERROR ORIGINAL: total = base - valor_impuesto (Restaba el impuesto en lugar de sumarlo). El código se ejecutaba sin fallar pero daba un total erróneo.
# CORRECCIÓN: Se cambió a 'base + valor_impuesto'.
# --------------------------------------------------------------------------
total = base + valor_impuesto

# Salida de datos
print()
print("-----------------------------")
print("RESUMEN DE COMPRA CORREGIDO")
print("-----------------------------")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"TOTAL: ${total}")

