#Dado n > 0, inteiro e x real (float), calcular x / 2 – 3xˆ2/ 4 + 5xˆ3/ 8 – 7xˆ4/ 16 + . . . ± (2n-1) xˆn/ 2ˆn

def soma_serie_3(n,x):

    #inicia a soma e as outras variáveis
    soma, pot, sinal, num, den = 0, x, 1, 1, 2

    #variar k de 1 até n e somar os termos
    for k in range (1, n+1):
        soma = soma + num*pot*sinal/den
        num = num + 2
        pot = pot*x
        den = den*2
        sinal = - sinal
        
    print ("O valor da soma é:", soma)

soma_serie_3(3,3)

