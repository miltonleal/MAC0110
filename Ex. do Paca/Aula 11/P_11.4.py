#Dado n, inteiro maior que zero imprimir tabela com os valores de x * y para x e y = 1, 2, ..., n.
#Imprimir apenas o triângulo superior

def main ():

    # ler n inteiro >= 0
    n = int(input("Entre com o valor de n inteiro > a zero: "))

    #imprimir o cabeçalho
    print ("     ", end = '')
    for horiz in range (1, n + 1):
        print ("%5d" %horiz, end = '')
    print()

    # Variar i de 1 até n. Para cada i, variar j de 1 até i.
    # Para cada para (i, j) imprimir i * j

    for vert in range (1, n+1):
        print ("%5d" %vert, end = '')

        k = vert - 1
        if k == 0:
            for j in range (1, n+1): print("%5d" %(vert*j), end = '')
            print()

        else:
            p = 1
            while p <= k:
                print ("     ", end = '')
                p += 1

            for j in range(p, n + 1): print("%5d" % (vert * j), end='')
            print()



while True:
    main ()


