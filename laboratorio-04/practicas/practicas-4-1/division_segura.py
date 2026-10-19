try:
    dividendo = float(input("Dividendo: "))
    divisor = float(input("Divisor: "))
except ValueError:
    print("La entrada no puede convertirse a número.")
else:
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    else:
        print("Resultado:", resultado)

