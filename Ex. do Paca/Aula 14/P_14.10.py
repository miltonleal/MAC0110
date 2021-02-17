#Função Seno(x, epsilon) que calcula a soma dos n primeiros termos da série do seno.
#sen(x) = x / 1! – xˆ3/ 3! + xˆ5/ 5! - . . . + (-1)k. xˆ2k+1 / (2k+1)! + . . . até encontrar um termo em módulo menor que epsilon.

def funcao_seno (x,eps):

    num = x
    sinal = 1
    k = 1
    fat = 1
    soma = 0


    while True:

        termo = num * sinal / fat

        if abs(termo) < eps:
            return soma

        soma = soma + num*sinal/fat
        num = num * x * x
        sinal = - sinal
        fat = fat * (2 * k) * (2 * k + 1)
        k = k + 1

print (funcao_seno(1,0.00000001))
