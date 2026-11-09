exemplares = 8

retirar = int(input("Você deseja quantos exemplares? "))

if retirar <= 0:
    print("Seu pedido é inválido, certifique-se que seu número é maior do que 0.")
elif retirar > exemplares:
    print("Não há exemplares o suficiente.")
else:
    print("Pedido confirmado!")
    print(f"Estoque atualizado, agora você tem {exemplares - retirar} exemplares.")