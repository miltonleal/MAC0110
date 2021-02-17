#A função conta_elementos acima, conta sempre a partir do elemento 0 da lista.
# Faça uma pequena modificação de modo que ela conte de um índice inicial até um índice final,
# ou seja, conta_elementos(a, inicio, fim).

def conta_elementos(a,inicio,fim,x):

    cont = 0

    for k in range (len(a)):

        if k >= inicio and k <= fim:
            if a[k] == x:
                cont = cont + 1
    return cont

a = [0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4]

print (conta_elementos(a,0,13,2))


