# Função Seno(x, n) que calcula a soma dos n primeiros termos da série do seno.
#sen(x) = x / 1! – xˆ3/ 3! + xˆ5/ 5! - . . . + (-1)k. xˆ2k+1 / (2k+1)! + . . .

def funcao_seno (x,n):

    num = x
    sinal = 1
    k = 1
    fat = 1
    soma = 0


    while k <= n:

        soma = soma + num*sinal/fat
        num = num * x * x
        sinal = - sinal
        fat = fat*(2*k)*(2*k+1)
        k = k + 1

    return soma

print (funcao_seno(100,15))


