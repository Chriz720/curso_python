#ao invés disso:
""" produto_preco = 12.00
produto_quantidade = 5
produto_preco2 = 13.00
produto_quantidade2 = 6
produto_preco3 = 14.00
produto_quantidade3 = 7
produto_preco4 = 15.00
produto_quantidade4 = 8

print(f"Valor total do produto 1: {produto_preco * produto_quantidade}")
print(f"Valor total do produto 2: {produto_preco2 * produto_quantidade2}")
print(f"Valor total do produto 3: {produto_preco3 * produto_quantidade3}")
print(f"Valor total do produto 4: {produto_preco4 * produto_quantidade4}") """

#podemos utilizar isso:
""" def total_venda(valor, quantidade):
    return valor * quantidade

preco = float(input("Digite o preço do produto: R$ "))
qtd = int(input("Digite a quantidade vendida: "))

print(f"O valor da venda ficou: R$ {total_venda(preco, qtd)}") """

#para definir o nome da classe ela precisa estar com a primeira letra maiúscula
#Este é um exemplo de classificador:
""" class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def resumo(self):
        print("----------------------------------------")
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco}")
        print(f"Qtd. Estoque: {self.estoque} unidades")

    def vender(self, quantidade):
        if quantidade <= 0:
            return "Erro: Quantidade inválida!"
        elif quantidade > self.estoque:
            return "Erro: Estoque insuficiente!"
        else:
            self.estoque -= quantidade
            return f"Venda realizada!\nValor da venda: R$ {self.preco * quantidade}"


produto1 = Produto("Caderno", 12.0, 5 )
produto2 = Produto("Caneta", 3.0, 10)
produto3 = Produto("Folha", 6.0, 8)

produto1.resumo()
print()
print(produto1.vender(5))
produto1.resumo

produto2.resumo()
print()
print(produto2.vender(3))
produto2.resumo

produto3.resumo()
print()
print(produto3.vender(2))
produto3.resumo """

#que é a mesma coisa do que:
""" print(f"Nome: {produto1.nome}")
print(f"Preço: {produto1.preco}")
print(f"Qtd estoque: {produto1.estoque} unidades")
print("-------------------------------")
print(f"Nome: {produto2.nome}")
print(f"Preço: {produto2.preco}")
print(f"Qtd estoque: {produto2.estoque} unidades")
print("-------------------------------")
print(f"Nome: {produto3.nome}")
print(f"Preço: {produto3.preco}")
print(f"Qtd estoque: {produto3.estoque} unidades") """

#exemplo de orientação a objetos
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.status = "Pendente"
        
    def resumo(self):
        print(f"Descrição: {self.descricao}\nStatus: {self.status}")

    def concluir(self):
        if self.status == "Concluída":
            return f"{self.descricao} já está concluída!"
        
        self.status = "Concluída"
        return f"{self.descricao} concluída com sucesso!"

tarefa1 = Tarefa("Aprender Python")
tarefa2 = Tarefa("Estudar Lógica de Programação")
tarefa3 = Tarefa("Baixar GTA VI")
tarefa4 = Tarefa("Achar Easter Eggs")

#Aqui ele printa a primeira verificação
print("\nAntes")
tarefa1.resumo()
print(tarefa1.concluir())
tarefa1.resumo
print("Depois\n")

#Aqui ele printa a segunda que já confere e diz que a tarefa já está concluída
print("\nAntes")
tarefa1.resumo()
print(tarefa1.concluir())
tarefa1.resumo
print("Depois\n")