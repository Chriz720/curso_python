sul = 15.00
sudeste = 20.00
centro_oeste = 25.00
norte_nordeste = 35.00

valor_compra = float(input("Digite o valor da compra: "))
frete = input("Digite a região de entrega (sul, sudeste, centro-oeste, norte/nordeste): ").lower()

if valor_compra >= 300.00:
    print("O frete é gratuito.")
elif valor_compra <= 0:
    print("Valor de compra inválido.")
if frete == "sul":
    valor_total = valor_compra + sul
    print(f"O valor total da compra com frete é: R$ {valor_total:.2f}")
elif frete == "sudeste":
    valor_total = valor_compra + sudeste
    print(f"O valor total da compra com frete é: R$ {valor_total:.2f}")
elif frete == "centro-oeste":
    valor_total = valor_compra + centro_oeste
    print(f"O valor total da compra com frete é: R$ {valor_total:.2f}")
elif frete == "norte" or frete == "nordeste":
    valor_total = valor_compra + norte_nordeste
    print(f"O valor total da compra com frete é: R$ {valor_total:.2f}")
else:
    print("Região de entrega inválida.")