#A função arctangente de x para |x| < 1 pode ser calculada por: arctan (x) = x – xˆ3/ 3 + xˆ5/ 5 – xˆ7/ 7 + . . .
#Função Arctang(x, n) que calcula a soma dos n primeiros termos da série do arctangente.

def funcao_arctang (x,n):

    soma = 0
    num = x
    sinal = 1
    k = 1

    while k <= n:
        soma = soma + (num*sinal)/((2*k)-1)
        num = num * x * x
        sinal = - sinal
        k = k + 1

    return soma

print (funcao_arctang(0.8,200))


