CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


def validar_texto(valor, campo):
    if not isinstance(valor, str) or valor.strip() == "":
        raise ValueError(f"El {campo} no puede estar vacío.")
    return valor.strip()


def validar_categoria(categoria):
    if categoria not in CATEGORIAS:
        raise ValueError(
            "Categoría no permitida. Opciones: " + ", ".join(CATEGORIAS)
        )
    return categoria


def validar_precio(precio):
    if isinstance(precio, bool) or not isinstance(precio, (int, float)):
        raise ValueError("El precio debe ser un número.")
    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero.")
    return precio


def validar_cantidad(cantidad):
    if isinstance(cantidad, bool) or not isinstance(cantidad, int):
        raise ValueError("La cantidad debe ser un número entero.")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    return cantidad


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        self._codigo = validar_texto(codigo, "código")
        self._nombre = validar_texto(nombre, "nombre")
        self._categoria = validar_categoria(categoria)
        self._precio = validar_precio(precio)
        self._cantidad = validar_cantidad(cantidad)

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        try:
            self._cantidad = validar_cantidad(nueva_cantidad)
        except ValueError:
            return False
        return True

    def actualizar_precio(self, nuevo_precio):
        try:
            self._precio = validar_precio(nuevo_precio)
        except ValueError:
            return False
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad
