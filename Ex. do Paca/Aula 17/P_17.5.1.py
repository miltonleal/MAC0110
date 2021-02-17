#eliminar repetidos. varrendo a lista do fim para o início. Nessa solução a ordem dos elementos é mantida.


a = [0,3,0,3,2,0, 34, 1,2,1,2,1,3,2]

def elimina_repetidos (a):

    k = 1

    while k <= len(a) - 1:
        if a[len(a)-k] in a[0:len(a)-k]:
            del a[len(a)-k]
        else: k += 1

elimina_repetidos(a)

print (a)
