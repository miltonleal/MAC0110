#Função subtracao(a, b) que devolve uma lista c que é a diferença dos conjuntos a e b (a -b).

def elimina_repetido(a):

    k = len(a)
    i = 0
    result = []

    while i < k:

        if not (a[i]) in a[i+1:]:
            result.append(a[i])
        i = i +1
    return result

def subtracao(a, b):
    # inicia c com a
    c = []

    # varre b - insere b[k] em c se não estiver em a
    for k in range(len(a)):
        if a[k] not in b: c.append(a[k])

    # retorna o c = a unido com b

    c.sort()
    return elimina_repetido(c)

a = [1,2]
b = [5,5,2,0]

print(subtracao(a,b))
