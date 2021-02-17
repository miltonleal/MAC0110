# Construa uma tabela para x = 0, 0.01, 0.02, ..., 0,10 com o valor de x1, x2, ..., x10.

import math

print ("Valores de X        Valores de X elevado às potências de 1 a 10")
print ()

def main ():

    for i in range (0,11):
        i_aux = i/100
        for j in range (0,11):
            k= math.pow(i_aux, j)
            print ("%8.3f%43.20f" %(i_aux,k))

main()