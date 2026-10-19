def duplicar(numero):
    resultado = numero * 2
    return resultado


doble = duplicar(8)
print(doble)

try:
    print(resultado)
except NameError as error:
    print("Error esperado:", error)

