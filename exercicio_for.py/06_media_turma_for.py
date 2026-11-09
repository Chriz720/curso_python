soma = 0
notas_a_partir_de_sete = 0
aluno = int(input("Digite a quantidade de alunos: "))

for aluno in range(1, aluno + 1):
    print("Aluno:", aluno)
    nota = float(input("Digite uma nota de 0 a 10: "))

    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida. Digite uma nota de 0 a 10: "))

    soma += nota

    if nota >= 7:
        notas_a_partir_de_sete += 1

media = soma / 4

print("Média da turma:", media)
print("Quantidade de notas a partir de 7:", notas_a_partir_de_sete)