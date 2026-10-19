nombre_producto = "Monitor Gamer"
precio = 100000.0
cantidad = 2
porcentaje_descuento = 0.10


porcentaje_impuesto = 0.19


subtotal = precio * cantidad
valor_descuento = subtotal * porcentaje_descuento
total_con_descuento = subtotal - valor_descuento


base_descuento = total_con_descuento
valor_impuesto = base_descuento * porcentaje_impuesto
total_final = base_descuento + valor_impuesto


print(f"Producto: {nombre_producto}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Total: ${total_con_descuento}")


print("\n--- Reto Adicional ---")
print(f"Base después del descuento: ${base_descuento}")
print(f"Valor del impuesto (19%): ${valor_impuesto}")
print(f"Total final: ${total_final}")

