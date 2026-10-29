encontrado = False

for tentativa in range(1, 4):
    print("Tentativa:", tentativa)
    codigo = input("Digite o código de acesso: ")

    if codigo == "ROBO123":
        encontrado = True   
        break

    print("Código incorreto.")

if encontrado:
    print("Acesso autorizado.")
else:
    print("Tentativas esgotadas.")