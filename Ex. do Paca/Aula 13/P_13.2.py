##  Calcular o valor máximo e mínimo da função sen x * cos x, no intervalo [0, 2π]. Usar passo de 0.001

import math

def func(func):

    for i in range(0, 6283):
        i_aux = i/1000
        func = math.sin(i_aux)*math.cos(i_aux)
        a = max (math.sin(0)*math.cos(0), math.sin(i_aux)*math.cos(i_aux))

    print (a)

func(func)
