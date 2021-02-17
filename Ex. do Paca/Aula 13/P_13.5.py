# Dado N, simule a jogada de um dado (faces 1 a 6) N vezes e calcule quantas vezes cada face ocorreu

import random

def main ():

    n = int(input("Digite o valor de n: "))
    a = 1

    soma_1 = 0
    soma_2 = 0
    soma_3 = 0
    soma_4 = 0
    soma_5 = 0
    soma_6 = 0

    while a <= n:

        k = random.randrange(1,7)
        if k == 1: soma_1 += 1
        elif k == 2: soma_2 += 1
        elif k == 3: soma_3 += 1
        elif k == 4: soma_4 += 1
        elif k == 5: soma_5 += 1
        elif k == 6: soma_6 += 1
        a += 1

    print("Face     Nº de vezes")
    print("%3d%12d\n%3d%12d\n%3d%12d\n%3d%12d\n%3d%12d\n%3d%12d" % (1,soma_1, 2, soma_2, 3, soma_3, 4, soma_4, 5, soma_5, 6, soma_6))
main ()
