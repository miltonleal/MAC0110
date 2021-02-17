#A função ln x para 0 < x ≤ 2 pode ser calculada por: ln(x) = (x-1) - (1/2)(x-1)2 + (1/3)(x-1)ˆ3 + (1/4)(x-1)4 + ...
# P14.17) Função Logn(x, n) que calcula a soma dos n primeiros termos da série do logaritmo natural.

def funcao_logn(x,n):

    soma = 0
    sinal = 1
    num = x-1
    k = 1


    while k <= n:

        soma = soma + num*sinal/k
        num = num * num
        k = k+1
        sinal = - sinal

    return soma

print (funcao_logn(2,1000000))

