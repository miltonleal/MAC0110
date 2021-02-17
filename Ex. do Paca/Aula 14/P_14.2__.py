#Dado n > 0, inteiro e x real (float), calcular x – xˆ2/ 2 + xˆ3/ 3 – xˆ4/ 4 + . . . ± xˆn/ n. quando 0<x<=1
def soma_serie_2(x,eps):

    #inicia a soma
    soma, pot, k = 0, x, 1

    #variar k de 1 até n e somar os termos
    while True:
        termo = pot/k
        soma = soma + pot/k
        #alterna o sinal da potência de x
        pot = -pot*x
        k = k+1
        if termo < eps:
            return soma

    #imprime o resultado
print ("O valor da soma é:", soma_serie_2(0.5,0.0001))
print ("O valor da soma é:", soma_serie_2(0.6,0.0001))
print ("O valor da soma é:", soma_serie_2(0.7,0.0001))
print ("O valor da soma é:", soma_serie_2(0.8,0.0001))
print ("O valor da soma é:", soma_serie_2(0.9,0.0001))
print ("O valor da soma é:", soma_serie_2(0.99,0.0001))




