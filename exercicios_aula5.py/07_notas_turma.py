qtd = input("Digite a quantidade de alunos: ")
notas = []

for i in range(int(qtd)):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
    while nota < 0 or nota > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        notas[i] = nota
        
print(f"Notas dos alunos: {notas}")
print(f"Média da turma: {sum(notas) / len(notas)}")
print(f"Maior nota da turma: {max(notas)}")
print(f"Menor nota da turma: {min(notas)}")
print(f"Quantidade de alunos com nota maior ou igual a 7: {len([nota for nota in notas if nota >= 7])}")