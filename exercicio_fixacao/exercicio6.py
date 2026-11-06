idade = int(input("Digite a idade do usuário: "))
matricula = input("O usuário está matriculado? (sim/nao): ")
autorizacao = input("O usuário tem autorização do professor? (sim/nao): ")
disponivel = input("O laboratório está disponível? (sim/nao): ")

if disponivel.lower() == "sim" and idade >= 16 and matricula.lower() == "sim" and autorizacao.lower() == "sim":
    print("O usuário pode utilizar o laboratório.")
elif idade < 16 or matricula.lower() != "sim" or autorizacao.lower() != "sim" or disponivel.lower() != "sim":
    print("O usuário não pode utilizar o laboratório.")
else:
    print("O usuário não pode utilizar o laboratório.")