#Dado n > 0, inteiro e x real (float), calcular x / 2 – 3xˆ2/ 4 + 5xˆ3/ 8 – 7xˆ4/ 16 + . . . ± (2n-1) xˆn/ 2ˆn quando 0<x<=1

def soma_serie_3(x,eps):

    #inicia a soma e as outras variáveis
    soma, pot, sinal, num, den = 0, x, 1, 1, 2

    #variar k de 1 até n e somar os termos
    while True:
        termo = num*pot*sinal/den
        soma = soma + num*pot*sinal/den
        num = num + 2
        pot = pot*x
        den = den*2
        sinal = - sinal
        if termo < eps:
            return soma


print ("O valor da soma é:", soma_serie_3(0.5,0.0001))
print ("O valor da soma é:", soma_serie_3(0.6,0.0001))
print ("O valor da soma é:", soma_serie_3(0.7,0.0001))
print ("O valor da soma é:", soma_serie_3(0.8,0.0001))
print ("O valor da soma é:", soma_serie_3(0.9,0.0001))


