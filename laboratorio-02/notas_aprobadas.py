
numeros = [3, 8, 12, 5, 20, 7]
mayores = [numero for numero in numeros if numero >= 10]
print(mayores)

notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]

aprobadas = [nota for nota in notas if nota >= 3.0]
reprobadas = [nota for nota in notas if nota < 3.0]
dobles = [nota * 2 for nota in notas]

print("Aprobadas:", aprobadas)
print("Inferiores a 3.0:", reprobadas)
print("Multiplicadas por 2:", dobles)

estados = ["Aprobado" if nota >= 3.0 else "No aprobado" for nota in notas]
print(estados)

