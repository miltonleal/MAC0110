# Dado n > 0, inteiro e x real (float), calcular x + xˆ3/ 3 + xˆ5/ 5 + . . . + xˆ2n-1/ (2n-1)

def soma_serie_1(n,x):

    #inicia a soma
    soma = 0

    #variar k de 1 até n e somar cada termo
    for k in range (1, n+1):
        soma = soma + pow(x, 2*k-1)/(2*k-1) #também poderia ser escrito como soma + (x**(2*k-1))/(2*k-1)

    #imprime o resultado
    print ("O valor da soma é:", soma)

soma_serie_1(3,3)

