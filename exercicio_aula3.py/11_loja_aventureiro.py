nome = input("Qual é o seu nome aventureiro? ")
ouro = int(input("Quanto de ouro você tem? "))

if ouro < 0:
    print("Quantidade de ouro inválida")
else: 
    print("\n=====LOJA=====\n")
    
    print("Digite 1 para comprar poção de vida. (25 moedas)")
    print("Digite 2 para comprar escudo. (60 moedas)")
    print("Digite 3 para comprar espada. (100 moedas)\n")

opcao = input("Digite sua opção: ")
p1o = 25
s2o = 60
t3o = 100

if opcao == "1":
    if ouro >= p1o:
        print(f"Parabéns por sua compra! Você tem agora {ouro - p1o} moedas!")
    else:
      print("Infelizmente você não tem moedas o suficiente.")
      print(f"Ainda lhe faltam {p1o - ouro} moedas.") 

elif opcao == "2":
    if ouro >= s2o:
        print(f"Parabéns por sua compra! Você tem agora {ouro - s2o} moedas!")
    else:
        print("Infelizmente você não tem moedas o suficiente.")
        print(f"Ainda lhe faltam {s2o - ouro} moedas.") 

elif opcao == "3":
    if ouro >= t3o:
        print(f"Parabéns por sua compra! Você tem agora {ouro - t3o} moedas!")
    else: 
         print("Infelizmente você não tem moedas o suficiente.")
         print(f"Ainda lhe faltam {t3o - ouro} moedas.") 

else: 
    print("Item inválido.")