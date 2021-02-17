#A função arctangente de x para |x| < 1 pode ser calculada por: arctan (x) = x – xˆ3/ 3 + xˆ5/ 5 – xˆ7/ 7 + . . .
#Função Arctang(x, epsilon) que calcula a mesma soma até encontrar um termo em módulo menor que epsilon

def funcao_arctang (x,eps):

    soma = 0
    num = x
    sinal = 1
    k = 1

    while True:
        termo = (num*sinal)/((2*k)-1)

        if abs(termo) < eps:
            return soma

        soma = soma + (num*sinal)/((2*k)-1)
        num = num * x * x
        sinal = - sinal
        k = k + 1

    return soma

print (funcao_arctang(0.8,0.000000001))


