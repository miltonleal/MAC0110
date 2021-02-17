#Dado n > 0, inteiro e x real (float), calcular x + xˆ2/2! + xˆ3/3! + xˆ4/4! + . . . + xˆn/n! quando 0<x<=1


def soma_serie_4(x,eps):

    #inicia a soma e próximo termo
    soma = 0
    fat = 1
    pot = x
    k = 1

    #variar k de 1 até n
    while True:
        termo = (pot/fat)
        fat = fat * k
        soma = soma + (pot/fat)
        pot = pot *x
        if termo < eps:
            return soma
        k = k+1

print ("O valor da soma é:", soma_serie_4(0.5,0.0001))
print ("O valor da soma é:", soma_serie_4(0.6,0.0001))
print ("O valor da soma é:", soma_serie_4(0.7,0.0001))
print ("O valor da soma é:", soma_serie_4(0.8,0.0001))
print ("O valor da soma é:", soma_serie_4(0.9,0.0001))
