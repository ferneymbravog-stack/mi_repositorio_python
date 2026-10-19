nombre = str(input("Escribe tu nombre: "))
horas_trabajadas = int(input("Escribe las horas trabajadas: "))
Valor_hora = float(input("Escribe el valor por hora: "))

total_pago = horas_trabajadas * Valor_hora

print("=============================")
print("     RESUMEN PAGO     ")
print("=============================")
print("Nombre:", nombre)
print("Horas trabajadas:", horas_trabajadas)
print("Valor por hora:", Valor_hora)
print("Total a pagar: $", total_pago)