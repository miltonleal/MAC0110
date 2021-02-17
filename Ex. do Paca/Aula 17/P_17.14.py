# Função elimina_repetidos(x) que devolve uma lista contendo os elementos da lista x sem repetição.

a = [1,1,1,1,1,2,3,4,5]

def elimina_repetidos(a):

    i = 0
    result = []

    for i in range (len(a)):

    #while i < len(a):

        if not (a[i] in a[i+1:]):
            result.append(a[i])
        i += 1
    return result


print (elimina_repetidos(a))

