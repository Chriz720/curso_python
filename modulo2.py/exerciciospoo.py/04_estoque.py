class Produto:
    def __init__(self, preco, estoque):
        self.preco = preco
        self.estoque = estoque

    def repor(self, quantidade):
        if quantidade <= 0:
            return "Erro: Quantidade inválida!"

        self.estoque += quantidade
        return "Reposição realizada!"

    def vender(self, quantidade):
        if quantidade <= 0:
            return "Erro: Quantidade inválida!"
        elif quantidade > self.estoque:
            return "Erro: Estoque insuficiente!"

        self.estoque -= quantidade
        return f"Venda realizada!\nValor da venda: R$ {self.preco * quantidade}"

    def valor_em_estoque(self):
        return self.preco * self.estoque


produto = Produto(5.0, 4)

retorno = produto.vender(2)
print(f"Retorno: {retorno}; estoque: {produto.estoque}")

retorno = produto.vender(3)
print(f"Retorno: {retorno}; estoque: {produto.estoque}")

retorno = produto.repor(5)
print(f"Retorno: {retorno}; estoque: {produto.estoque}")

retorno = produto.repor(0)
print(f"Retorno: {retorno}; estoque: {produto.estoque}")

print(f"Valor em estoque: R$ {produto.valor_em_estoque()}")