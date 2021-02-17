#Função sub_pol(a, b) que devolve lista contendo a diferença dos polinômios a e b.

a = [1,1,0]
b = [1,2,2]

def sub_pol(a,b):

    if len(a) > len(b):
        c = a[:]
        for k in range (len(b)):
            c[k] = c[k] - (b[k])

    else:
        c = b[:]
        for k in range (len(a)):
            c[k] = a[k] - (c[k])

    for k in range (len(c)-1):
        if c[-1] == 0: del c[-1]
        else: break

    return c

print (sub_pol(a,b))
