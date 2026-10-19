import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not isinstance(codigo, str) or codigo.strip() == "":
            raise ValueError("El código es obligatorio.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre es obligatorio.")
        if categoria not in CATEGORIAS:
            raise ValueError("La categoría no es válida.")
        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = self._validar_precio(precio)
        self._cantidad = self._validar_cantidad(cantidad)

    @staticmethod
    def _validar_precio(precio):
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if not math.isfinite(precio):
            raise ValueError("El precio debe ser un número finito.")
        if precio <= 0:
            raise ValueError("El precio debe ser positivo.")
        return float(precio)

    @staticmethod
    def _validar_cantidad(cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        return cantidad

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

    @property
    def valor_inventario(self):
        return self._precio * self._cantidad

    def actualizar_cantidad(self, nueva_cantidad):
        validada = self._validar_cantidad(nueva_cantidad)
        self._cantidad = validada

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
        )

    def __str__(self):
        return (
            f"{self.codigo} | {self.nombre} | {self.categoria} | "
            f"${self.precio} | {self.cantidad} unidades"
        )

