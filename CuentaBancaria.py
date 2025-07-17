
class CuentaBancaria:

    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, monto):
        self.saldo+= monto
        print(f"Se deposito {monto} correctamente")

    def retirar(self, monto):
        self.saldo-= monto
        print(f"Se retiro {monto} correctamente")

    def mostrar_saldo(self):
        print(f"Saldo Total: {self.saldo}")


cuenta = CuentaBancaria("Daniela Bravo")
cuenta.depositar(300)
cuenta.depositar(100)

cuenta.mostrar_saldo()
cuenta.retirar(50)
cuenta.mostrar_saldo()