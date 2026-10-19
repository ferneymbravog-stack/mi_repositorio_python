def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    return base * porcentaje / 100


precio = 100000
cantidad = 2
porcentaje_descuento = 10
porcentaje_impuesto = 19

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje_descuento)
base = subtotal - descuento
impuesto = calcular_impuesto(base, porcentaje_impuesto)
total = base + impuesto

print("Subtotal:", int(subtotal))
print("Descuento:", int(descuento))
print("Base después del descuento:", int(base))
print("Impuesto:", int(impuesto))
print("Total:", int(total))

