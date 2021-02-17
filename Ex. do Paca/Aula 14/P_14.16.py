#A função exponencial pode ser calculada por:eˆx = 1 + x + xˆ2/2! + xˆ3/ 3! + xˆ4/ 4! + ... + xˆn/ n! + ...
# P14.16) Função Expo(x, epsilon) que calcula a mesma soma até encontrar um termo em módulo menor que
# epsilon


def funcao_expo (x,eps):

    soma = 1
    fat = 1
    k = 1
    num = x

    while True:

        termo = num/fat
        if abs(termo) < eps:
            return soma

        soma = soma + num/fat
        num = num * x
        k = k + 1
        fat = fat * k

print (funcao_expo(31,0.00001))
