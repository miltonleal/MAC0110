#Escreva uma função SomaSerie(x, n) que recebe um valor float x e um int n > 0.
# Devolve o valor da soma abaixo:
# x/2 – 3x2/4 + 5x3/8 – 7x4/16 + . . . ± (2n-1)xn/2n

def SomaSerie(x,n):

    # inicia a soma e as outras variáveis
    soma, pot, sinal, num, den = 0, x, 1, 1, 2

    for k in range (1, n+ 1): #variar k de 1 até n e somar os termos
        soma += (num * pot * sinal) / den #soma da expressão
        num += 2 #soma o numerador
        pot *= x #multiplica o x por ele mesmo
        den *= 2 #multiplica o denominador
        sinal *= -1 #troca o sinal
    return soma

print(SomaSerie(0.1,100))