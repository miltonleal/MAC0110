#O cosseno pode ser calculado por: cos(x) = 1 – xˆ2/2! + xˆ4/4! – xˆ6/6! + . . . + (-1)k . xˆ2k/(2k)! + . . .
#Função Cosseno(x, epsilon) que calcula a mesma soma até encontrar um termo em módulo menor que epsilon.

def funcao_cosseno (x,eps):

    num = 1
    sinal = 1
    k = 1
    fat = 1
    soma = 0


    while True:

        termo = num*sinal/fat

        if abs(termo) < eps:
            return soma

        soma = soma + num*sinal/fat
        num = num * x * x
        sinal = - sinal
        fat = fat * (2*k-1) * (2*k)
        k = k+1

print (funcao_cosseno(1, 0.0000000001))


