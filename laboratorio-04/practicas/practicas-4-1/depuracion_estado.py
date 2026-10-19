class Producto:
    def __init__(self, cantidad):
        self._cantidad = cantidad

    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            print("Cantidad inválida.")
            return
        self._cantidad = nueva_cantidad


try:
    int("hola")
except ValueError:
    print("No se pudo convertir.")

producto = Producto(5)
producto.actualizar_cantidad(-3)
print(producto._cantidad)
producto.actualizar_cantidad(8)
print(producto._cantidad)

