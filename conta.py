class Conta:
    def __init__(self, numero:int, saldo:float):
        self.numero = numero
        self.limite = 100
        self.extrato = []
        self.saldo = saldo + self.limite

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite
    print("VC eh um Bacana")