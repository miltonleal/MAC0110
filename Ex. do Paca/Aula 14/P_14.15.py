#A função exponencial pode ser calculada por:eˆx = 1 + x + xˆ2/2! + xˆ3/ 3! + xˆ4/ 4! + ... + xˆn/ n! + ...
# P14.15) Função Expo(x, n) que calcula a soma dos n primeiros termos da série da exponencial

def funcao_expo (x,n):

    soma = 1
    fat = 1
    k = 1
    num = x

    while k <= n:

        if n == 1:
            return 1

        else:

            soma = soma + num/fat
            num = num * x
            k = k + 1
            fat = fat * k

    return soma

print (funcao_expo(5,80))


