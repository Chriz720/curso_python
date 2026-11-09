idade = int(input("Digite sua idade: "))

if idade <= 0:
    print("Idade inválida, digite uma idade acima de 0.")
elif idade < 12 or idade >= 60:
    print("Entrada gratuita.")
else:
    print("Você terá que pagar R$ 20,00") 