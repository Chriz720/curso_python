nome = input("Digite o nome do seu personagem: ")
nivel = int(input("Digite o nível de seu personagem: "))

if nivel < 1:
    print("Nível menor do que 1, registro inválido.")
elif nivel <= 5:
    print(f"Seu nome é {nome} e sua classificação é Aprendiz!")
elif nivel <= 15:
    print(f"Seu nome é {nome} e sua classificação é Guerreiro!")
elif nivel <= 30:
    print(f"Seu nome é {nome} e sua classificação é Veterano")
else:
    print(f"Seu nome é {nome} e sua classificação é Lendário")