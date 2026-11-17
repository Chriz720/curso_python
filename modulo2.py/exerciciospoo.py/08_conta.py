class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldoi = 0

    def depositar(self, valor):
        if valor <= 0:
            return False
        else: 
            self.saldoi += valor
            return True
        
    def sacar(self, valor):
        if valor <= 0 or valor > self.saldoi:
            return False
        else:
            self.saldoi -= valor
            return True
   
    def resumo(self):
        print(self.titular)
        print(self.saldoi)

conta1 = Conta("Karlos")
conta1.depositar(50)
conta1.sacar(20)
conta1.sacar(40)
conta1.depositar(-10)
conta1.resumo()

conta2 = Conta("Gioerge")
conta2.resumo()