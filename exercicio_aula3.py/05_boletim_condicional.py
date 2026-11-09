trabalho = float(input("Nota do trabalho: "))
prova = float(input("Nota da prova: "))
media = float((trabalho + prova) / 2)

if trabalho < 0 or trabalho > 10 or prova < 0 or prova > 10:
    print("Nota inválida.")
    print("Operação encerrada.")
elif media >= 7:
    print("Aprovado.")
    print("Operação encerrada.")
elif media >= 5:
    print("Em recuperação.")
    print("Operação encerrada.")
else:
    print("Reprovado.") 
    print("Operação encerrada.")