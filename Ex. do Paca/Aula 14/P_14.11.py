#O cosseno pode ser calculado por: cos(x) = 1 – xˆ2/2! + xˆ4/4! – xˆ6/6! + . . . + (-1)k . xˆ2k/(2k)! + . . .
#Função Cosseno(x, n) que calcula a soma dos n primeiros termos da série do cosseno.

def funcao_cosseno (x,n):

    num = 1
    sinal = 1
    k = 1
    fat = 1
    soma = 0


    while k <= n:

        soma = soma + num*sinal/fat

        num = num * x * x

        sinal = - sinal

        fat = fat * (2*k-1) * (2*k)

        k = k+1

    return soma

print (funcao_cosseno(1, 15))






