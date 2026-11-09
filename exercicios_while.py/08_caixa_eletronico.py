saldoi = 500.00
nd = 0
sd = 0
while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo é de {saldoi}R$")

    elif opcao == "2":
        deposito = float(input("Digite um valor para depositar: "))

        if deposito < 0:
            print("O valor do depósito deve ser maior que 0.")
        else:
             print("Depósito evetivado!")

             saldoi += deposito
             nd += 1
             print(f"Número de depósitos realizados: {nd}")

    elif opcao == "3":
            saque = float(input("Digite um valor para sacar: "))
    
            if saque < 0:
                print("O valor do saque deve ser maior que 0.")
            elif saque > saldoi:
                 print("O valor do saque não pode exceder o valor do saldo.")
            else:
                 print("Saque efetivado!")

                 saldoi -= saque
                 sd += 1
                 print(f"Número de saques realizados: {sd}")

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")