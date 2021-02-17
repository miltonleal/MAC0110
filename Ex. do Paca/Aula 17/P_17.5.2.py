#Para cada elemento a[k] (k = 0, 1, ...), procure a partir de a[k+1] todos os iguais a a[k] e os elimine.

a = [0,0,2,2,3,2,2,3,1,1,2]

def elimina_iguais(a):

    k = 0

    while k < len(a) -1:
        if a[k] in a[k+1:]:
            del a[k]
        else: k = k +1

elimina_iguais(a)

print (a)




