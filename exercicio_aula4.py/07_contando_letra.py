palavra = input("Digite uma palavra: ")
l = input("Digite uma letra: ")
qtd_letra = 0

for letra in palavra:
    
    if letra == l:
        qtd_letra += 1

print(f"Foram encontradas {qtd_letra} letras!")