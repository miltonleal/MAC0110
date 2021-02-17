# Escreva uma função que recebe 3 valores reais a, b e c e devolve as raízes da equação
# ax2+bx+c=0. Devolve também um parâmetro adicional que diz o tipo de raízes.

import math

def RaizesEquacaoSegundoGrau(a, b, c):
    '''Calcula as raízes reais de equação do 2 Grau.'''
    if a == 0 and b == 0: return -3, None, None
    if a == 0: return -2, -c / b, None
    delta = b * b - 4 * a * c
    if delta < 0: return -1, None, None
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return 0, x1, x2
# exemplo de chamada
print("Raizes:", RaizesEquacaoSegundoGrau(1, 0, 2))

#exemplo de chamada
r, z1, z2 = RaizesEquacaoSegundoGrau(1, 0, 2)
if r == 0: print("Raizes:", z1, "e ", z2)
elif r == -1: print("Não tem raizes reais")
elif r == -2: print("Equação do Primeiro Grau - Raiz:", z1)
else: print("Não e' equação")