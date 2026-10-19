
ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

mayores_for = []
for venta in ventas:
    if venta["total"] > 100000:
        mayores_for.append(venta["producto"])

mayores = [venta["producto"] for venta in ventas if venta["total"] > 100000]
print("Con for:        ", mayores_for)
print("Con comprensión:", mayores)

categorias = {venta["categoria"] for venta in ventas}
producto_y_valor = {venta["producto"]: venta["total"] for venta in ventas}
valores = [venta["total"] for venta in ventas]
total_ventas = sum(valores)

print("Categorías diferentes:", categorias)
print("Producto y valor:", producto_y_valor)
print("Suma de todas las ventas:", total_ventas)

