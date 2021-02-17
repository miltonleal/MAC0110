

def FF(L):
    if len(L) == 0: return 0
    return L[0] + FF(L[1:])

#print(FF([1, 2, 3]))
s = []
#print(FF(s))
t = [-1, -2]
#print(FF(t))

def FF_non_recursive(L):

    soma = 0 #inicia a soma com zero
    for k in range(len(L)): #varre a lista
        soma += L[k] #soma os elementos
    return soma

print(FF_non_recursive(t))

t = [-1, -2]





