# quantos elementos em entre 0 e 9, 10 e 19, ... , 90 e 99

def main():

    n = int(input("Entre com n > 0 inteiro:"))

    # 10 contadores - f[0..9] - f[i] = quantos entre 10*i e 10 * i + 9
    f = 10 * [0]

    # ler os n números e para cada um incrementar o contador correspondente

    for i in range(n):
        x = int(input("entre com novo valor:"))
        k = x // 10
        f[k] = f[k] + 1

    # imprime os 10 contadores

    for i in range(10):
        print("Há ", f[i], "elementos entre ", i * 10, " e ", i * 10 + 9)

main()