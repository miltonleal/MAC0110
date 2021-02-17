# Dado um número inteiro n ≥ 0, calcular o fatorial de n (n!)

def main ():

    n = int(input("Digite o valor de n: "))

    #inicia as variáveis

    fat = i = 1

    while i < n:
        i += 1
        fat *= i
    # resultado

    print ("O valor de %d! é =" %n, fat)

main ()

