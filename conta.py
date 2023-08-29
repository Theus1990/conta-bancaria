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


    def sacar(self, valor: float):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append("-Saldo")
            return True
        else:
            return False


    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.extrato.append("+ Depositar")
            return True
        else: 
            return False