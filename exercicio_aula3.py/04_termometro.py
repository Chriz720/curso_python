temperatura = float(input("Digite a temperatura: "))

if temperatura <= 18:
    print("Ambiente frio")
elif temperatura >= 26:
    print("Ambiente quente")
else:
    print("Ambiente agradável")