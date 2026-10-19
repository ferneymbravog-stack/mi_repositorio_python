
unidades_disponibles = 12
unidades_solicitadas = 8

hay_suficientes = unidades_disponibles >= unidades_solicitadas
son_iguales = unidades_disponibles == unidades_solicitadas
se_pidio_de_mas = unidades_solicitadas > unidades_disponibles

print("¿Hay suficientes unidades?", hay_suficientes)
print("¿Las cantidades son iguales?", son_iguales)
print("¿Se solicitaron más de las disponibles?", se_pidio_de_mas)


