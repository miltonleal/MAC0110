# Dados i e j (1 <= i, j <= 6), simule a jogada de 2 dados 1000 vezes
# e diga quantas vezes ocorreu o par i, j de faces.

import random

def main():

    a = 1

    soma_1_1 = 0
    soma_1_2 = 0
    soma_1_3 = 0
    soma_1_4 = 0
    soma_1_5 = 0
    soma_1_6 = 0

    while a <= 1000:

        k = random.randrange(1, 7)
        if k == 1:
            g = random.randrange(1, 7)
            if g == 1:
                soma_1_1 += 1
            elif g == 2:
                soma_1_2 += 1
            elif g == 3:
                soma_1_3 += 1
            elif g == 4:
                soma_1_4 += 1
            elif g == 5:
                soma_1_5 += 1
            elif g == 6:
                soma_1_6 += 1
            a += 1
            continue
        a += 1

    print(" Faces     Nº de vezes")
    print("%6s%10d\n%6s%10d\n%6s%10d\n%6s%10d\n%6s%10d\n%6s%10d" % (
    "1 e 1", soma_1_1, "1 e 2", soma_1_2, "1 e 3", soma_1_3, "1 e 4", soma_1_4, "1 e 5", soma_1_5, "1 e 6", soma_1_6))
    print("\nTotal de jogadas com pares que tenham 1:", soma_1_1+soma_1_2+soma_1_3+soma_1_4+soma_1_5+soma_1_6)

main()

