class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)

    def quantidade_alunos(self):
        return len(self.alunos)

#a partir desse momento eu separo as turmas
turma1 = Turma("Python")
turma2 = Turma("Java")

turma1.matricular("Ordelí")
turma1.matricular("Melmel")
turma2.matricular("Luís")

for turma in (turma1, turma2):
    print(f"Turma: {turma.nome}")
    print(f"Alunos: {turma.alunos}")
    print(f"Quantidade de alunos: {turma.quantidade_alunos()}")
