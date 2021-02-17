# Dado N, decompor N em seus fatores primos, e imprimir tabela

def main ():

    n = int(input("digite o valor de n: "))

    print ("Primo     Expoente")

    conta = 0

    for k in range(2, n + 1):

        # verifica se k tem divisores entre 2 e a raiz de k
        div = 2  # primeiro candidato a divisor
        tem_div = False

        while div * div <= k:
            if k % div == 0:
                tem_div = True  # achou um divisor
                break  # sai do while
            div += 1  # testa o próximo candidato a divisor

            # verifica se encontrou algum divisor entre 2 a raiz de k
            # ou seja, se saiu do while pelo break ou não
        if not tem_div and n % k == 0:
            conta = conta +1
            print("%3d%11dx" % (k,n/k))

    print ()
while True:
    main ()
