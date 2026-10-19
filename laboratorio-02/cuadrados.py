
numeros = [1, 2, 3, 4, 5]

cuadrados = []
for numero in numeros:
    cuadrados.append(numero ** 2)
print(cuadrados)

cuadrados = [numero ** 2 for numero in numeros]
print(cuadrados)
print(numeros)

cuadrados_dict = {numero: numero ** 2 for numero in [1, 2, 3, 4]}
print(cuadrados_dict)

grupos = [[1, 2], [3, 4], [5, 6]]
aplanada = [numero for grupo in grupos for numero in grupo]
print(aplanada)

generador = (numero ** 2 for numero in range(1, 5))
print(type(generador))
print(list(generador))
tupla_cuadrados = tuple(numero ** 2 for numero in range(1, 5))
print(tupla_cuadrados)

