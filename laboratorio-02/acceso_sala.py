
edad = int(input("Edad: "))
autorizacion = input("¿Tiene autorización? (si/no): ").strip().lower()

if edad >= 18:
    print("Puede ingresar a la sala.")
elif autorizacion == "si":
    print("Puede ingresar a la sala con autorización.")
else:
    print("Acceso no permitido.")

