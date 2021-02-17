#escreva a função SomaSerie(x, eps) que recebe um valor float x e um float eps > 0
# (eps é um número próximo de zero) e calcule a soma de todos os termos que sejam maiores
# ou iguais a eps em módulo.

def SomaSerie(x,eps):

    #inicia a soma e as outras variáveis
    soma, pot, sinal, num, den = 0, x, 1, 1, 2

    while True:  #loop que realiza a soma da série

            soma += (num * pot * sinal) / den  #soma da expressão
            num += 2  #soma o numerador
            pot *= x  #multiplica o x por ele mesmo
            den *= 2  #multiplica o denominador
            sinal *= -1  #troca o sinal
            if abs(num * pot * sinal / den) < eps:  #compara o último termo com o valor do eps
                return soma

print (SomaSerie(0.1,0.000000000000000000000000000000001))
