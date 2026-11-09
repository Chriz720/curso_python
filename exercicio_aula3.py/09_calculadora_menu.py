nd1 = float(input("Digite o primeiro número que você deseja calcular: "))
nd2 = float(input("Digite o segundo número que você deseja calcular: "))

print("\n=====MENU=====\n")

print("Digite '1' para somar.")
print("Digite '2' para subtrair.")
print("Digite '3' para multiplicar.")
print("Digite '4' para dividir.\n")

operacao = int(input("Digite sua operação: "))

if operacao == 1:
    print(f"Seu resultado foi: {nd1 + nd2}")
elif operacao == 2:
    print(f"Seu resultado foi: {nd1 - nd2}")
elif operacao == 3:
    print(f"Seu resultado foi: {nd1 * nd2}")
elif operacao == 4:
    if nd2 != 0:
        print(f"Seu resultado foi: {nd1 / nd2}")
    else:
        print("Não é possível dividir número por zero.")
else:
    print("Operação inválida.")