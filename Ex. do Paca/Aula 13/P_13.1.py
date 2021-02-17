# Calcular os valores da função senx*cosx para x = 0, 0.001, 0.002, ..., 2π

import math

def func():

    for i in range(0, 6283):
        i_aux = i/1000
        f = math.sin(i_aux)*math.cos(i_aux)
        print ("O valor da função senx*cosx é =", f, "quando o x =", i_aux)

func()

