#Dado n ≥ 0 calcular os fatoriais dos números de 0 a n

def main():
    ''' Dado n>=0 inteiro, calcular os fatoriais de 0 a n '''
    # ler n inteiro >= 0
    n = int(input("Entre com o valor de n inteiro >= a zero: "))

    # Variar k de 0 a n e para cada k calcular k!
    for k in range(n + 1):
        # calcular k!
        kfat = 1
        for j in range(2, k + 1):
            kfat *= j
        # imprime o valor de k!
        print("%d! = " %k, kfat)

main()