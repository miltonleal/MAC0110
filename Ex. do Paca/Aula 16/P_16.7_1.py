#Números no intervalo [0, 100). Quantos estão nos intervalos [0, 10), [10, 20), [20, 30), ..., [90, 100)

import math

def main():

    n = int(input("Entre com n > 0 inteiro:"))

    # 10 contadores - f[0..9] - f[i] = quantos entre 10*i e 10 * i + 9
    f = 10 * [0]

    # ler os n números e para cada um incrementar o contador correspondente

    for i in range(n):
        x = float(input("entre com novo valor:"))
        k = math.trunc(x // 10)
        f[k] = f[k] + 1

    # imprime os 10 contadores

    for i in range(10):
        print("Há ", f[i], "elementos entre [", i * 10,",", i * 10 + 10,")")



main()