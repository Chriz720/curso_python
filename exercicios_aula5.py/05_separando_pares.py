numero = [int(input("Digite um número: ")) for _ in range(8)]

pares = [num for num in numero if num % 2 == 0]

print(f"Números digitados: {numero}")
print(f"Números pares digitados: {pares}")