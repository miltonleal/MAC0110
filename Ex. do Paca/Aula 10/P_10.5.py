#  Calcular o valor da função x^3 + x^2+ x + 1 para x = 1, -1, 2, -2, 3, -3

def main ():

    for k in [1,-1,2,-2,3,-3]:
        print ("O valor de x quando vale %d é =" %k, k*k*k + k*k + k + 1)

main ()

