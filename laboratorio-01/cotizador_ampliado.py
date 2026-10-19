print("=============================")
print("  COTIZADOR PYTHON AMPLIADO  ")
print("=============================")
print()

codigo_cotizacion = input("Código de la cotización: ")
nombre_vendedor = input("Nombre del vendedor: ")
nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento (%): "))
porcentaje_impuesto = float(input("Impuesto (%): "))
costo_envio = float(input("Costo de envío: "))


subtotal = precio_unitario * cantidad
valor_descuento = subtotal * (porcentaje_descuento / 100)
base = subtotal - valor_descuento
valor_impuesto = base * (porcentaje_impuesto / 100)

total_final = base + valor_impuesto + costo_envio


print()
print("-----------------------------")
print("RESUMEN DE COTIZACIÓN")
print("-----------------------------")
print(f"Código cotización: {codigo_cotizacion}")
print(f"Vendedor         : {nombre_vendedor}")
print(f"Cliente          : {nombre_cliente}")
print(f"Producto         : {producto}")
print(f"Precio unitario  : ${precio_unitario}")
print(f"Cantidad         : {cantidad}")
print(f"Subtotal         : ${subtotal}")
print(f"Descuento        : ${valor_descuento}")
print(f"Base             : ${base}")
print(f"Impuesto         : ${valor_impuesto}")
print(f"Costo de envío   : ${costo_envio}")
print(f"TOTAL FINAL      : ${total_final}")

