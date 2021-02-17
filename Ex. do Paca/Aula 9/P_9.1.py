# P9.1) Dado N > 0 e uma sequência de N números calcular a soma dos elementos da sequência.

def main ():

    #lê a quantidade de elementos da sequência

    N = int(input("Digite o número de elementos da sequência: "))

    while True:

        if N <= 0: N = int(input("O número inserido não é maior que zero.\nPor favor, digite novamente o número de elementos da sequência: "))

        cont, soma = 1, 0

        while cont <= N:
            x = int (input("Digite o próximo elemento da sequência: "))
            soma += x
            cont += 1
        print ("O valor da soma dos", N, "elementos da sequência é:", soma)

main ()

