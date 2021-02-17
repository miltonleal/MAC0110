# Escreva uma função que recebe n maior que zero e devolve o valor da soma: 1/1! + 1/2! + 1/3! + ... + 1/n!

import math

def main ():

    print(somainvfat (sum))

def somainvfat (sum):

    n = int(input("Digite o valor de n: "))
    soma = 0

    for i in range (0, n + 1):

        soma = soma + 1/ math.factorial(i)
    return soma

main ()
