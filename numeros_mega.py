'''
import random

def gerar_numeros_baseados_em_resultados(resultados_anteriores):
    if len(resultados_anteriores) < 10:
        print("Por favor, forneça pelo menos 8 resultados anteriores.")
        return

    numeros_baseados_em_resultados = []

    for _ in range(6):
        resultado_escolhido = random.choice(resultados_anteriores)
        numero_escolhido = random.choice(resultado_escolhido)
        numeros_baseados_em_resultados.append(numero_escolhido)

    return sorted(numeros_baseados_em_resultados)

if __name__ == "__main__":
    resultados_anteriores = [
        [1, 10, 20, 30, 40, 50],
        [2, 15, 25, 35, 45, 55],
        [17, 26, 45, 46, 48, 53],
        [1, 3, 23, 27, 47, 57],
        [4, 17, 29, 30, 52, 58],
        [10, 20, 30, 42, 47, 53],
        [3, 11, 42, 45, 46, 57],
        [7, 18, 20, 26, 38, 51],
        [10, 13, 16, 18, 37, 54],
        [3, 7, 32, 34, 42, 54],
        [4, 6, 14, 19, 22, 29],
        [1, 26, 31, 34, 42, 45], 

        list(range(61))
    ]
    numeros_gerados = gerar_numeros_baseados_em_resultados(resultados_anteriores)
    print("Números baseados nos resultados anteriores:", numeros_gerados)
'''





