#  Dado n ≥ 0 e x diferente de zero, inteiros, calcular x^n sem usar a função interna pow do Python

def main ():

    x = float(input("Digite o número que você quer exponencializar: "))
    n = int(input("Digite o expoente: "))

    pot = 1

    for k in range(0, n):
        pot = pot * x

    print ("O valor de %1.10f elevado a %d é" %(x,n), pot)

main ()

