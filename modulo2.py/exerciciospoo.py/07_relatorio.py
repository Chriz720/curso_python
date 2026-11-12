class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

produto1 = Produto("Caderno", 10.0, 2)
produto2 = Produto("Caneta", 3.0, 0)
produto3 = Produto("Borracha", 2.0, 5)

produtos = [produto1, produto2, produto3]
estoque_zero = 0
total = 0

for produto in produtos:
    if produto.estoque == 0:
        estoque_zero += 1
    total += produto.preco * produto.estoque

print(f"Quantidade de produtos sem estoque: {estoque_zero}")
print(f"Total em estoque: R$ {total}")