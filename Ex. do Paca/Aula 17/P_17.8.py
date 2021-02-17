'''Idem, imprimindo apenas uma linha para cada elemento repetido, isto é, se o elemento aparece k
vezes, imprimir a linha com a quantidade apenas na primeira vez que ele aparece. Já resolvemos esse
problema anteriormente. Basta para cada elemento verificar se ele já apareceu antes. Use também a
função conta_elementos acima.'''

a = [3,3,3,2,2,3,5,4,4,4,4,4,2,2,2,2,3,3,3,5,5]

def conta_elementos(a,x):

    cont = 0

    for k in range(len(a)):
        if a[k] == x:
            cont = cont + 1
    return cont

def imprime_repetidos(a):

    k = 0
    guarda_numeros_que_sairam = []

    while k < len(a):

        if a[k] not in guarda_numeros_que_sairam:

            print("Elemento", a[k], "ocorre", conta_elementos(a, a[k]), "vezes")
            guarda_numeros_que_sairam.append(a[k])

        k = k +1

imprime_repetidos(a)
