# Dado n > 0, inteiro e x real (float), calcular x + xˆ3/ 3 + xˆ5/ 5 + . . . + xˆ2n-1/ (2n-1) quando 0 < x <= 1

def soma_serie_1(x, eps):

    #inicia a soma
    soma = 0
    k = 1


    #variar k de 1 até n e somar cada termo

    while True:
        termo = pow(x, 2 * k - 1) / (2 * k - 1)
        soma = soma + termo #também poderia ser escrito como soma + (x**(2*k-1))/(2*k-1)
        k = k + 1
        if termo < eps:
            return soma

#imprime o resultado
print ("O valor da soma é:", soma_serie_1(0.99,0.0001))



