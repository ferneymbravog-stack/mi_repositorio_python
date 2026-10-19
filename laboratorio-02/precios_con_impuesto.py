
precios = [10000, 20000, 50000, 80000]

con_impuesto_for = []
for precio in precios:
    con_impuesto_for.append(precio * 1.19)

con_impuesto_comp = [precio * 1.19 for precio in precios]

print("Con for:        ", con_impuesto_for)
print("Con comprensión:", con_impuesto_comp)
print("¿Son equivalentes?", con_impuesto_for == con_impuesto_comp)

