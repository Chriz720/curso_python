nome = input("Digite o nome do personagem: ")
vida = int(input("Digite a vida atual do personagem: "))
ataque = int(input("Digite os pontos de ataque do personagem: "))
v_inimigo = int(input("Digite os pontos de vida do inimigo: "))
d_inimigo = int(input("Digite os pontos de defesa do inimigo: "))

dano = ataque - d_inimigo

if vida <= 0:
    print(f"{nome} não poderá atacar.")
elif dano <= 0:
    print(f"{nome} não causará dano ao inimigo.")
elif dano >= v_inimigo:
    print(f"{nome} causou {dano} de dano e derrotou o inimigo.")
else:
    print(f"{nome} causou {dano} de dano ao inimigo.")
    print(f"Vida restante do inimigo: {v_inimigo - dano}")