#Função trans_lista_em_conjunto(c) que devolve uma lista contendo os elementos da lista c,
# sem repetição e classificada em ordem crescente.
# Se a lista c possui elementos com tipo diferente devolve a lista vazia [].


def elimina_repetido(a):

    k = len(a)
    i = 0
    result = []

    while i < k:

        if not (a[i]) in a[i+1:]:
            result.append(a[i])
        i = i +1
    return result

def trans_conjunto(c):

    if c == []: return []

    tipo = type(c[0])

    for k in range (1,len(c)):
        if not (type(c[k] is tipo)): return []

    r = elimina_repetido(c)

    r.sort()
    return r


print (trans_conjunto([10,20,30,40,10,10]))


