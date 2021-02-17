#Dado n > 0, inteiro e x real (float), calcular x – xˆ2/ 2 + xˆ3/ 3 – xˆ4/ 4 + . . . ± xˆn/ n.

def soma_serie_2():

    #ler n inteiro > 0
    n = int(input("Digite o valor de n > 0 inteiro: "))

    #ler o x float
    x = float(input("Digite o valor de x: "))

    #inicia a soma
    soma, pot = 0, x

    #variar k de 1 até n e somar os termos
    for k in range (1, n+1):
        soma = soma + pot/k

        #alterna o sinal da potência de x
        pot = -pot*x

    #imprime o resultado
    print ("O valor da soma é:", soma)

soma_serie_2()


