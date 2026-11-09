#while significa "enquanto", e for significa "para tal coisa"
#while serve para fazermos repetições
contador = 1

while contador <= 5:
    print(contador)
    contador += 1

print("Fim!")

#Aqui é um exemplo de looping
#Dica: para interromper uma execução que ficou presa em um loop infinito, normalmente utilizamos Ctrl + C no terminal.

i = 0

while i <= 0:
    print("teste")
    i -= 1

#o break point é uma ferramenta no executar e depurar onde consigo ver o passo a passo do código
#exemplo de break point e while
contador = 1

while contador <= 5:
    print("A contagem está em", contador)
    contador += 1

print("Fim")

#Um acumulador guarda um resultado que vai sendo atualizado a cada repetição.
#Exemplo: solicitar três números e calcular sua soma.
contador = 1
soma = 0

while contador <= 3:
    numero = int(input("Digite um número: "))

    soma += numero
    contador += 1

print("Soma total:", soma)

#break para o looping, fazendo assim que não se repita o while
while True:
    resposta = input("Deseja continuar? (sim/nao): ")

    if resposta == "nao":
        break

    print("Continuando...")

print("Programa encerrado!")

#exemplo completo
while True:
    print("\n=== MENU ===")
    print("1 - Dizer olá")
    print("2 - Calcular o dobro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá! Seja bem-vindo!")

    elif opcao == "2":
        numero = int(input("Digite um número: "))
        print("Dobro:", numero * 2)

    elif opcao == "0":
        print("Encerrando...")
        break
    
    else:
        print("Opção inválida!")