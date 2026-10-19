def calcular_unidades(productos):
    total = 0
    for producto in productos:
        total += producto["cantidad"]
    return total


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 7},
]
print(calcular_unidades(inventario))


def agregar(nombre, nombres):
    nombres.append(nombre)


productos = ["Teclado"]
agregar("Mouse", productos)
print(productos)


def agregar_en_copia(nombre, nombres):
    copia = nombres.copy()
    copia.append(nombre)
    return copia


original = ["Teclado"]
nueva = agregar_en_copia("Mouse", original)
print("Original:", original)
print("Nueva:", nueva)


def agotados(productos):
    nombres = []
    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])
    return nombres


def agotados_comprension(productos):
    return [p["nombre"] for p in productos if p["cantidad"] == 0]


datos = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Monitor", "cantidad": 0},
]
print(agotados(datos))
print(agotados_comprension(datos))

