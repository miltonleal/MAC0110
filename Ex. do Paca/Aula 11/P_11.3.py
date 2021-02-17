#Dado n, inteiro maior que zero imprimir tabela com os valores de x * y para x e y = 1, 2, ..., n.
#Imprimir apenas o triângulo inferior

def main ():

    # ler n inteiro >= 0
    n = int(input("Entre com o valor de n inteiro > a zero: "))

    #imprimir o cabeçalho
    print ("     ", end = '')
    for i in range (1, n + 1):
        print ("%5d" %i, end = '')
    print ()

    # Variar i de 1 até n. Para cada i, variar j de 1 até i.
    # Para cada para (i, j) imprimir i * j

    for i in range (1, n + 1):
        print ("%5d" %i, end = '')
        for j in range (1, i + 1): print ("%5d" %(i*j), end = '')
        print ()
    print ()

while True:
    main ()


