class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1

    def zerar(self):
        self.valor = 0


primeiro = Contador()
segundo = Contador()

for _ in range(3):
    primeiro.incrementar()
segundo.incrementar()

print(primeiro.valor, segundo.valor)

primeiro.zerar()

print(primeiro.valor, segundo.valor)