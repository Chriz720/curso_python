numero = [int(input("Digite um número: ")) for _ in range(6)]

print(f"Números digitados: {numero}")
print(f"Maior número digitado: {max(numero)}")
print(f"Menor número digitado: {min(numero)}")
print(f"Soma dos números digitados: {sum(numero)}")
print(f"Média dos números digitados: {sum(numero) / len(numero)}")