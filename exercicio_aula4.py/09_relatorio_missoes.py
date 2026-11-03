energia = 100
missao = 25
pontos = 0
qtd_pontos = 0
missoes_realizadas = 0
media = 0

if energia <= 0:
        print("Energia esgotada! Missão não pode continuar.")
else:
    for i in range(1, 6):
        if energia < 25:
            print("Energia esgotada! Missão não pode continuar.")
            break
        pontos = int(input("Digite a quantidade de pontos (0 a 100): "))
        while pontos < 0 or pontos > 100:
            pontos = int(input("Pontos inválidos. Digite a quantidade de pontos (0 a 100): "))
            
        qtd_pontos += pontos
        missoes_realizadas += 1
        energia -= missao

if missoes_realizadas > 0:
    media = qtd_pontos / missoes_realizadas

print("=====RELATÓRIO DE MISSÕES=====\n")
print(f"Missões realizadas: {missoes_realizadas}")
print(f"Pontuação total: {qtd_pontos}")
print(f"Média de pontos: {media:.2f}")
print(f"Energia restante = {energia}")  
print("=================================")