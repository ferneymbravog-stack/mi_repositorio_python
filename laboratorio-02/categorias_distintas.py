
categorias = ["Periféricos", "Accesorios", "Periféricos", "Componentes"]
unicas = {categoria for categoria in categorias}
print(unicas)

productos = [
    {"nombre": "Teclado", "categoria": "Periféricos"},
    {"nombre": "Mouse", "categoria": "Periféricos"},
    {"nombre": "Disco", "categoria": "Componentes"}
]
categorias_distintas = {producto["categoria"] for producto in productos}
print("Categorías distintas:", categorias_distintas)

productos = [
    {"codigo": "P001", "nombre": "Teclado"},
    {"codigo": "P002", "nombre": "Mouse"},
    {"codigo": "P003", "nombre": "Monitor"}
]
catalogo = {producto["codigo"]: producto["nombre"] for producto in productos}
print(catalogo)

