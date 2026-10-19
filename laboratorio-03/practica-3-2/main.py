import operaciones
from operaciones import calcular_subtotal, calcular_descuento

subtotal = operaciones.calcular_subtotal(85000, 3)
descuento = operaciones.calcular_descuento(subtotal, 10)

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total:", subtotal - descuento)

subtotal2 = calcular_subtotal(40000, 2)
descuento2 = calcular_descuento(subtotal2, 5)
print(subtotal2 - descuento2)

print(operaciones.calcular_subtotal(10000, 3))

