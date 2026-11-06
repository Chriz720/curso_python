usuario_correto = input("Informe seu usuário: ")
senha_correta = input("Informe sua senha: ")

if usuario_correto != "admin":
    print("Usuário não encontrado!")
else: 
    if senha_correta != "python123":
        print("Senha incorreta!")
    else:
        print("Acesso autorizado!")