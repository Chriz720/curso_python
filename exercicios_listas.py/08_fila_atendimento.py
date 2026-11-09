atendimento = []

print("1 - Adicionar pessoa ao final da fila")
print("2 - Atender a primeira pessoa da fila")
print("3 - mostrar a fila e sua quantidade de pessoas")
print("0 - Sair")

while True:
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome da pessoa: ")
        atendimento.append(nome)
        print(f"{nome} foi adicionado(a) ao final da fila.")
    elif opcao == "2":
        if atendimento:
            pessoa_atendida = atendimento.pop(0)
            print(f"{pessoa_atendida} foi atendido(a).")
        else:
            print("Não há pessoas na fila para atender.")
    elif opcao == "3":
        print(f"Fila atual: {atendimento}")
        print(f"Quantidade de pessoas na fila: {len(atendimento)}")
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")