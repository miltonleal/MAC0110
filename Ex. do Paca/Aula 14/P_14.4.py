#Dado n > 0, inteiro e x real (float), calcular x + xˆ2/2! + xˆ3/3! + xˆ4/4! + . . . + xˆn/n!

def soma_serie_4():

    #ler n inteiro > 0
    n = int(input("Digite o valor de n > 0 inteiro: "))

    #ler o x float
    x = float(input("Digite o valor de x: "))

    #inicia a soma e próximo termo
    soma = 0
    fat = 1
    pot = x

    #variar k de 1 até n
    for k in range (1, n+1):
        fat = fat * k
        soma = soma + (pot/fat)
        pot = pot *x

    print ("O valor da soma é:", soma)

soma_serie_4()

'''outra solução mais eficiente

def soma_serie_4():

    #ler n inteiro > 0
    n = int(input("Digite o valor de n > 0 inteiro: "))

    #ler o x float
    x = float(input("Digite o valor de x: "))

    #inicia a soma e próximo termo
    soma, termo = 0.0, 1.0 # inicia a soma e o termo

    #variar k de 1 até n
    for k in range (1, n+1):
        termo = termo * x / k
        soma = soma + termo

    print ("O valor da soma é:", soma)

soma_serie_4()




'''



