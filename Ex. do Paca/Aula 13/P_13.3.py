# Dado x >= 0, determinar para qual k, o valor de ex/k! fica menor que 10-5

import math

def main ():

    x = float(input("insira o valor de x: "))

    k = 0

    while True:

        a = math.exp(x)/math.factorial(k)
        if a < 0.00001:
            print("O valor de k! é:", k,"!")
            break
        k += 1

while True:
    main()