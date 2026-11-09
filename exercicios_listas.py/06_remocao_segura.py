nomes = ["Ana", "Bruno", "Ana", "Carla"]

print("Nomes na lista:")
for nome in nomes:
    print(nome)

remover_nome = input("Digite um nome para remover da lista: ")

if remover_nome in nomes:
    nomes.remove(remover_nome)
    print(f"O nome '{remover_nome}' foi removido da lista.")
else:
    print(f"O nome '{remover_nome}' não está na lista.")

print("Nomes restantes na lista:")
for nome in nomes:
    print(nome)