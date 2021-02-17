#Função soma_pol(a, b) que devolve lista contendo a soma dos polinômios a e b.
# recebe 2 polinômios (listas) a e b. Devolve c = a + b

a = [1,2,3,4]
b = [2,-2,4,-4]

def soma_pol(a,b):

    if len (a) > len(b):
        c = a[:]
        for k in range (len(b)): c[k] += b[k]
    else:
        c = b[:]
        for k in range (len(a)): c[k] += a[k]

    for k in range (len(c) -1):
        if c[-1] == 0: del c[-1]
        else: break

    return c

print (soma_pol(a,b))

