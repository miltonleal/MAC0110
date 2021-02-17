#Função interseccao(a, b) que devolve uma lista c que é a intersecção dos conjuntos a e b

def elimina_repetido(a):

    k = len(a)
    i = 0
    result = []

    while i < k:

        if not (a[i]) in a[i+1:]:
            result.append(a[i])
        i = i +1
    return result


def interseccao(a, b):
    # inicia c com a
    c = []
    k = 0

    for k in range(max(len(a),len(b))):

        if a[k] in b: c.append(a[k])

    c.sort()
    return elimina_repetido(c)

a = [1,2,3,4,5,7]
b = [2,4,5]

print (interseccao(a,b))

