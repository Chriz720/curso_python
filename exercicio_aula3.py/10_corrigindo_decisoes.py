idade = int(input("Idade: ")) #aqui deveria colocar como se o número fosse inteiro, pois todo input lê como se fosse uma string
autorizacao = input("Possui autorização? (sim/nao): ")

if idade >= 16 and autorizacao and "sim": #aqui ao invés do sinal de igualdade deveria colocar "and" para identificar que o aluno precisa ter a idade ideal e autorização
    print("Participação permitida.")
else: #a identação estava errada aqui, funções como if, elif e else não precisam de espaço
    print("Participação não permitida.") #agora os prints sim.