idade = int(input("Insira sua idade: "))
resposta = input("Possui inscrição? ")

if idade < 0:
    print("Idade inválida. Informe uma idade acima de 0.")
elif idade >= 14 and resposta == "sim":
     print("Parabéns! Você poderá participar!")
else:
     print("Você não poderá participar.")