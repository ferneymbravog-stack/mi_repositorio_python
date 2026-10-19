class RegistroCompartido:
    elementos = []


a = RegistroCompartido()
b = RegistroCompartido()
a.elementos.append("Teclado")
print("Lista compartida en el segundo:", b.elementos)


class Registro:
    def __init__(self):
        self.elementos = []


primero = Registro()
segundo = Registro()
primero.elementos.append("Teclado")
print("Primero:", primero.elementos)
print("Segundo:", segundo.elementos)


class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Hola,", self.nombre)


saludo = Saludo("Ana")
saludo.mostrar()


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombre)


Persona("Carlos").mostrar()

