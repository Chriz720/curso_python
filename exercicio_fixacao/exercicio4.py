salario = float(input("Digite o salário do cliente: "))
emprestimo = float(input("Digite o valor do empréstimo: "))
qtdp = float(input("Digite a quantidade de parcelas: "))

if salario < 2000.00:
    print("O empréstimo foi recusado.")
elif emprestimo * 10 > salario:
    print("O empréstimo foi recusado.")
elif qtdp < 1 or qtdp > 48:
    print("O empréstimo foi recusado.")
elif qtdp * 0.3 > salario:
    print("O empréstimo foi recusado.")
else:
    print("O empréstimo foi aprovado.")
