#Dado n e m maiores que zero e inteiros, imprimir uma tabela com os valores de x*y
# para x=1, 2, ..., n e y=1, 2, ... , m

def main ():

    #ler n e m inteiros >= 0
    n = int(input("Entre com o valor de n inteiro >= 0: "))
    m = int(input("Entre com o valor de m inteiro >= 0: "))

    #imprimir a linha de cabeçalho
    print("     ", end = '')
    for i in range (1, m + 1): print("%5d" %i, end = '')
    print()

    #variar i de 1 até n. Para cada i, variar j de 1 até m
    #para cada (i,j), imprimir i*j
    for i in range (1, n + 1):
        print ("%5d" %i, end = '')
        for j in range (1, m + 1): print ("%5d" %(i*j), end = '')
        print ()

while True:
    main ()

