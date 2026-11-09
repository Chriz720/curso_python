opcao = []

print("===== MENU =====\n")

print("1 - Registrar pontuação")
print("2 - Mostrar relatório")
print("3 - Desfazer o último registro")
print("0 - Sair")

pontos = []

while True:
    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        pontuacao = int(input("Digite a pontuação do jogador: "))
        if pontuacao < 0 or pontuacao > 100:
            print("Pontuação inválida. Digite um valor entre 0 e 100.")
        else:
            pontos.append(pontuacao)
            print(f"Pontuação {pontuacao} registrada com sucesso.")
    elif escolha == "2":
        if pontos:
            print(f"Pontuações registradas: {pontos}")
            print(f"Maior pontuação: {max(pontos)}")
            print(f"Menor pontuação: {min(pontos)}")
            print(f"Média das pontuações: {sum(pontos) / len(pontos)}")
            print(f"Quantidade de pontos maiores ou iguais a 70: {len([p for p in pontos if p >= 70])}")
        else:
            print("Nenhuma pontuação registrada ainda.")
    elif escolha == "3":
        if pontos:
            ultima_pontuacao = pontos.pop()
            print(f"Última pontuação {ultima_pontuacao} removida com sucesso.")
        else:
            print("Nenhuma pontuação registrada para desfazer.")
    elif escolha == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")