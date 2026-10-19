
productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

disponibles = [producto["nombre"] for producto in productos if producto["cantidad"] > 0]
print("Disponibles:", disponibles)

valores = [producto["precio"] * producto["cantidad"] for producto in productos]
print("Valor total:", sum(valores))

sin_existencias = [producto["nombre"] for producto in productos if producto["cantidad"] == 0]
precio_alto = [producto["nombre"] for producto in productos if producto["precio"] > 100000]
cantidades_distintas = {producto["cantidad"] for producto in productos}
nombre_y_precio = {producto["nombre"]: producto["precio"] for producto in productos}

print("Sin existencias:", sin_existencias)
print("Precio superior a $100.000:", precio_alto)
print("Cantidades diferentes:", cantidades_distintas)
print("Nombre y precio:", nombre_y_precio)

