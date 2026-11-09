while True:

    nota = int(input("Digite uma nota de 0 a 10: "))

    if nota >= 0 and nota <= 10:
        print("Nota registrada com sucesso!")
        break
    else:
        print("Nota inválida.")