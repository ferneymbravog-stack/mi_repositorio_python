class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje


moto1 = Motocicleta("Yamaha", "MT-07", 689)
moto2 = Motocicleta("Honda", "CB190R", 184)

for moto in (moto1, moto2):
    print(moto.marca, moto.modelo, moto.cilindraje)

