#Números no intervalo [0, 1000). Quantos estão nos intervalos [0, 100), [100, 200), ..., [900, 1000).

import math

def main():

    n = int(input("Entre com n > 0 inteiro:"))

    # 10 contadores - f[0..9] - f[i] = quantos entre 10*i e 10 * i + 9
    f = 10 * [0]

    # ler os n números e para cada um incrementar o contador correspondente

    for i in range(n):
        x = float(input("entre com novo valor:"))
        k = math.trunc(x // 100)
        f[k] = f[k] + 1

    # imprime os 10 contadores

    for i in range(10):
        print("Há ", f[i], "elementos entre [", i * 100,",", i * 100 + 100,")")

main()