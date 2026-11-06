hora = float(input("Digite quantas horas o carro ficou estacionado: "))

if hora <= 0:
    print("A quantidade de horas deve ser maior que zero.")
elif hora <= 2:
    print("Deverá pagar R$ 10,00.")
elif hora <= 5:
    print("Deverá pagar R$ 20,00.")
else:
    print("Deverá pagar R$ 30,00.")