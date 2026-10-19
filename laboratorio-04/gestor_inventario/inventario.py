from producto import Producto


class Inventario:
    def __init__(self):
        self._productos = []

    def registrar(self, producto):
        if self.buscar(producto.codigo) is not None:
            raise ValueError(f"Ya existe un producto con el código {producto.codigo}.")
        self._productos.append(producto)

    def buscar(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar(codigo)
        if producto is None:
            raise KeyError(codigo)
        producto.actualizar_cantidad(nueva_cantidad)

    def eliminar(self, codigo):
        producto = self.buscar(codigo)
        if producto is None:
            raise KeyError(codigo)
        self._productos.remove(producto)

    def listar(self):
        return list(self._productos)

    def sin_stock(self):
        return [producto for producto in self._productos if producto.cantidad == 0]

    def total_productos(self):
        return len(self._productos)

    def total_unidades(self):
        return sum(producto.cantidad for producto in self._productos)

    def valor_total(self):
        return sum(producto.valor_inventario for producto in self._productos)

    def categorias_utilizadas(self):
        return {producto.categoria for producto in self._productos}

    def exportar_datos(self):
        return [producto.a_diccionario() for producto in self._productos]

    @classmethod
    def desde_datos(cls, datos):
        if not isinstance(datos, list):
            raise ValueError("El contenido debe ser una lista de productos.")
        temporal = cls()
        for indice, registro in enumerate(datos, start=1):
            if not isinstance(registro, dict):
                raise ValueError(f"El registro {indice} no es un objeto válido.")
            try:
                producto = Producto.desde_diccionario(registro)
            except KeyError as error:
                raise ValueError(f"Al registro {indice} le falta el campo {error}.") from error
            except (TypeError, ValueError) as error:
                raise ValueError(f"Registro {indice} inválido: {error}") from error
            temporal.registrar(producto)
        return temporal

