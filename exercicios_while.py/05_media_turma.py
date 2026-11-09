alunos = int(input("Digite o número de alunos na turma: "))

if alunos <= 0:
    print("Número de alunos inválido, digite um valor maior que 0.")
else:
    soma = 0
    i = 1

    while i <= alunos:
        nota = float(input(f"Digite a nota do aluno {i}: "))

        if 0 <= nota <= 10:
            soma += nota
            print("Nota registrada com sucesso!")
            i += 1
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")

    media = soma / alunos

    print(f"\nMédia geral: {media:.2f}")
    print("Notas registradas com sucesso!")