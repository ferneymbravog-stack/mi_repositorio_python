class Inventario:
    def __init__(self):
        self._productos = []

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [
            producto.nombre
            for producto in self._productos
            if producto.cantidad == 0
        ]

    def resumen(self):
        categorias = {producto.categoria for producto in self._productos}
        return {
            "productos": len(self._productos),
            "unidades": sum(producto.cantidad for producto in self._productos),
            "valor": sum(producto.precio for producto in self._productos),
            "categorias": categorias,
        }

    def buscar_por_categoria(self, categoria):
        return [
            producto
            for producto in self._productos
            if producto.categoria == categoria
        ]

    def listar_ordenados_por_nombre(self):
        return sorted(self._productos, key=lambda producto: producto.nombre.lower())

    def actualizar_precio(self, codigo, nuevo_precio):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        return producto.actualizar_precio(nuevo_precio)

    def producto_mayor_valor(self):
        return max(
            self._productos,
            key=lambda producto: producto.calcular_valor(),
            default=None,
        )

    def nombres_por_codigo(self):
        return {producto.codigo: producto.nombre for producto in self._productos}
