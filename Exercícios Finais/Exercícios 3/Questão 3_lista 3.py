def func(L, x):

    if len(L) == 0: return -1
    k = len(L) - 1
    if L[k] == x: return k
    return func(L[:k], x)

#print(func([1, 2, 3], 2))

s = [5, 6, 5, 6]
#print(func(s, 5))


t = [2, 5, 7, 3]
#print(func(t, 3))

#função retorna o maior índice do elemento igual a x.

def func_non_recursive(L,x):

    for k in range (len(L)-1, -1, -1): #varre a lista de trás pra frente
        if L[k] == x: #compara o elemento da lista com x
            return k #retorna o índice do elemento se for igual a x


print(func_non_recursive(s, 6))







