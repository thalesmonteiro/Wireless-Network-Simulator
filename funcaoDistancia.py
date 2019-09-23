import math as math
#Verifica se um nó alcança outro
def alcance(centroX, centroY, raio, x, y):
    #calculo de distância usando a fórmula de distância entre dois pontos
    distancia = math.sqrt((centroX - x) ** 2 + (centroY - y) ** 2)
    #se alcancar retorna verdadeiro
    if(distancia <= raio):
        return True
    #caso contrario retorna falso
    else:
        return False 