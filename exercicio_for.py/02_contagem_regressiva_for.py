numero = int(input(f"Digite um número: "))

if numero <= 0:
        print("Valor inválido!")
for numero in range(numero + 1, -1, -1):
    print(numero)
    print("Lançamento realizado!")