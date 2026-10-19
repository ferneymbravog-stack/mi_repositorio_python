try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    print("La edad debe ser un número entero.")
else:
    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad > 120:
        print("La edad no puede ser mayor a 120.")
    else:
        print("Tu edad es:", edad)