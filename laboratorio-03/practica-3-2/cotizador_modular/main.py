import calculos
import validaciones


def main():
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        descuento = float(input("Descuento (%): "))
        impuesto = float(input("Impuesto (%): "))
    except ValueError:
        print("Debes escribir números válidos.")
        return

    if not validaciones.precio_valido(precio):
        print("El precio debe ser mayor que cero.")
        return
    if not validaciones.cantidad_valida(cantidad):
        print("La cantidad debe ser mayor que cero.")
        return
    if not (
        validaciones.porcentaje_valido(descuento)
        and validaciones.porcentaje_valido(impuesto)
    ):
        print("Los porcentajes deben estar entre 0 y 100.")
        return

    subtotal = calculos.calcular_subtotal(precio, cantidad)
    valor_descuento = calculos.calcular_descuento(subtotal, descuento)
    base = subtotal - valor_descuento
    valor_impuesto = calculos.calcular_impuesto(base, impuesto)
    total = base + valor_impuesto

    print("Subtotal:", subtotal)
    print("Descuento:", valor_descuento)
    print("Base después del descuento:", base)
    print("Impuesto:", valor_impuesto)
    print("Total:", total)


if __name__ == "__main__":
    main()

