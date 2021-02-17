#Função elimina_repetidos(x) que elimina todos os elementos repetidos da lista x.
# Ou seja, devolve a lista sem elementos repetidos

def elimina_repetidos(a):

    k = 0

    while k < len(a) -1:
        if a[k] in a[k+1:]:
            del a[k]
        else: k = k +1

x = [0,0,0,0,0,0,2,2,2,3,3,3,0,1]

elimina_repetidos(x)


print (x)

