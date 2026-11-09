#for funciona como o while, in é no e range serve para determinar até qual número irá se repetir. Exemplos de for:
""" for numero in range(1, 6):
    print(numero)

for numero in range(1, 11, 2):
    print(numero) """

#for com range e 1 argumento

#Significa que o range vai repetir 5 vezes, iniciando pelo 0, ou seja, {0, 1, 2, 3, 4}
""" for numero in range(5):
    print(numero, end=", ") """

#for com 2 argumentos

#significa que o range vai repetir 5 vezes (segundi argumento), começando pelo 0, ou seja, {0,1,2,3,4}, porém imprime a partir do 1 (primeiro argumento), sendo assim vai aparecer apenas {1, 2, 3, 4}
""" for numero in range(1, 5):
    print(numero, end=" ")   """

#for co 3 argumentos 
#significa que o range vai repetir 5 vezes, começandi pelo 0, ou seja, (0, 1, 2, 3, 4), porém imprime a partir do 1 (primeiro argumento) e pula de 2 em 2 (terceiro argumento)
""" for numero in range(1, 5, 2):
    print(numero, end=" ") """

#Exemplo de for na prática
""" numero = int(input("Digite um número inteiro: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado) """

#acumuladores e contadores
""" soma = 0
notas_a_partir_de_sete = 0

for aluno in range(1, 5):
    print("Aluno:", aluno)
    nota = float(input("Digite uma nota de 0 a 10: "))

    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida. Digite uma nota de 0 a 10: "))

    soma += nota

    if nota >= 7:
        notas_a_partir_de_sete += 1

media = soma / 4

print("Média da turma:", media)
print("Quantidade de notas a partir de 7:", notas_a_partir_de_sete) """

#O for também pode percorrer uma string, recebendo uma letra por vez:
""" palavra = "BATATA"

for letra in palavra:
    print(letra) """

#Exemplo com break
""" encontrado = False

for tentativa in range(1, 4):
    print("Tentativa:", tentativa)
    codigo = input("Digite o código de acesso: ")

    if codigo == "PYTHON":
        encontrado = True
        break

    print("Código incorreto.")

if encontrado:
    print("Acesso autorizado.")
else:
    print("Tentativas esgotadas.") """

#O continue pula o restante do bloco da repetição atual e passa para o próximo valor:
""" for numero in range(1, 6):
    if numero == 3:
        continue

    print(numero) """
