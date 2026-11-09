while True:
    print("\n=== MENU ===")
    print("1 - Somar dois números")
    print("2 - Verificar maioridade")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        n1 = float(input("Digite o 1° número: "))
        n2 = float(input("Digite o 2° número: "))
        print(f"{n1} + {n2} = {n1 + n2}")

    elif opcao == "2":
        idade = int(input("Digite sua idade: "))

        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")