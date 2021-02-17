#calcular a função soma_inv_fat(epsilon) que calcula a soma 1 + 2/2! + 3/3! + . . . + k/k! até encontrar um k tal que k/(k +1)! < epsilon

from math import factorial

def soma_inv_fat(epsilon):

    soma = 0
    k = 1

    while True:
        soma = soma + k/factorial(k)
        if k/factorial(k+1) < epsilon:
            return soma
        k = k + 1

print (soma_inv_fat(0.0003))


#sem usar a função fatorial

def soma_inv_fat(epsilon):

    soma = 0
    k = 1
    fat = 1

    while True:
        fat = fat * k
        soma = soma + k/fat
        k = k + 1
        if (k)/(fat*(k+1)) < epsilon:
            return soma

print (soma_inv_fat(0.0003))

