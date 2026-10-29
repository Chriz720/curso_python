soma = 0
numero_maior = 0

for numero in range(1, 7):
    print("Número", numero)
    numero = float(input("Digite um número: "))

    while numero < 0:
        numero = float(input("Número inválido. Digite novamente: "))
    soma = soma + numero
    
    if numero > 0:
        numero_maior += 1

print(f"Soma total: {soma}")
print(f"Quantidade de números maiores que zero: {numero_maior}")
