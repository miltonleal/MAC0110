#Repita agora o P17.8 com a nova função conta_elementos().

a = [3,3,3,2,2,3,5,4,4,4,4,4,2,2,2,2,3,3,3,5,5]


def conta_elementos(a,inicio,fim,x):

    cont = 0

    for k in range (len(a)):

        if k >= inicio and k <= fim:
            if a[k] == x:
                cont = cont + 1
    return cont

def imprime_repetidos(a):

    k = 0
    guarda_numeros_que_sairam = []

    while k < len(a):

        if a[k] not in guarda_numeros_que_sairam:

            print("Elemento", a[k], "ocorre", conta_elementos(a,2,10,a[k]), "vezes entre os índices[", 2, "] e [", 10, "]")
            guarda_numeros_que_sairam.append(a[k])

        k = k +1

imprime_repetidos(a)
