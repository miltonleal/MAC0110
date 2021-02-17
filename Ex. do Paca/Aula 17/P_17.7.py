#Função imprime_repetidos(a) que imprime a quantidade de vezes que cada elemento ocorre na lista a

a = [1,1,2,3,4,4,5]


def conta_elementos(a,x):

    cont = 0

    for k in range (len(a)):
        if a[k] == x:
            cont = cont + 1
    return cont

def imprime_repetidos(a):

    for k in range (len(a)):

        print ("Elemento", a[k], "ocorre", conta_elementos(a, a[k]), "vezes")

imprime_repetidos(a)