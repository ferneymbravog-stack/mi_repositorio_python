class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False
        self._saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0 or monto > self._saldo:
            return False
        self._saldo -= monto
        return True

    def consultar_saldo(self):
        return self._saldo


ana = Billetera("Ana")
luis = Billetera("Luis")

print("Ingreso Ana 100000:", ana.registrar_ingreso(100000))
print("Gasto Ana 30000:", ana.registrar_gasto(30000))
print("Gasto Ana 500000:", ana.registrar_gasto(500000))
print("Ingreso Ana -5:", ana.registrar_ingreso(-5))
print("Ingreso Luis 20000:", luis.registrar_ingreso(20000))
print("Gasto Luis 5000:", luis.registrar_gasto(5000))

print("Saldo de", ana.titular + ":", ana.consultar_saldo())
print("Saldo de", luis.titular + ":", luis.consultar_saldo())

