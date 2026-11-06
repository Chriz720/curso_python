lado_1 = int(input("Digite o valor do lado 1 do triângulo: "))
lado_2 = int(input("Digite o valor do lado 2 do triângulo: "))
lado_3 = int(input("Digite o valor do lado 3 do triângulo: "))

equilatero = lado_1 == lado_2 == lado_3
if equilatero:
    print("O triângulo é equilátero.")
isosceles = lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3
if isosceles and not equilatero:
    print("O triângulo é isósceles.")
if not equilatero and not isosceles:
    print("O triângulo é escaleno.")
else:
    print("O triângulo é inválido.")