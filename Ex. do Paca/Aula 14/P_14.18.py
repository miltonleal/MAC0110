#A função ln x para 0 < x ≤ 2 pode ser calculada por: ln(x) = (x-1) - (1/2)(x-1)2 + (1/3)(x-1)ˆ3 + (1/4)(x-1)4 + ...
#  Função Logn(x, epsilon) que calcula a mesma soma até encontrar um termo em módulo menor que
# epsilon.

def funcao_logn(x,eps):

    soma = 0
    sinal = 1
    num = x-1
    k = 1


    while True:

        termo = num*sinal/k
        if abs(termo) < eps:
            return soma

        soma = soma + num*sinal/k
        num = num * num
        k = k+1
        sinal = - sinal


print (funcao_logn(2,0.0000001))
