#Função uniao(a, b) que devolve uma lista c que é a união dos conjuntos a e b.

# recebe 2 conjuntos (listas) a e b. Devolve lista c = a unido com b

def elimina_repetido(a):

    k = len(a)
    i = 0
    result = []

    while i < k:

        if not (a[i]) in a[i+1:]:
            result.append(a[i])
        i = i +1
    return result

def uniao(a, b):
    # inicia c com a
    c = a[:]

    # varre b - insere b[k] em c se não estiver em a
    for k in range(len(b)):
        if b[k] not in a: c.append(b[k])

    # retorna o c = a unido com b

    c.sort()
    return elimina_repetido(c)

a = [1,2,2,2,3,4]
b = [5,5,2,0]

print(uniao(a,b))


