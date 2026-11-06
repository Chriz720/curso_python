mochila = ["corda", "água", "mapa", "água"]

print("Itens na mochila:")
for item in mochila:
    print(item)

encontrar_item = input("Digite um item para vrificar quantas vezes ele aparece na mochila: ")
quantidade = mochila.count(encontrar_item)

print(f"O item '{encontrar_item}' aparece {quantidade} vezes na mochila.")

if quantidade > 0:
        print(f"O item '{encontrar_item}' está na mochila.")
else:
        print(f"O item '{encontrar_item}' não está na mochila.")