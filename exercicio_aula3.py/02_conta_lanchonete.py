preco = float(input("Digite o valor do lanche: R$ "))
qtd = int(input("Digite a quantidade do lanche "))
total = preco * qtd
desc = total * 0.10
valor_final = total - desc

if total < 50:
    print(f"\nValor final da compra: {total} R$.")
else:
    print(f"\nValor da compra: {total} R$.")

    print("\nVocê recebeu 10% de desconto!")
    print(f"Seu desconto ficou de: {desc} R$")
    print(f"Valor final da compra: {valor_final} R$")