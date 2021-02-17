# Função seq_crescente(lista_num) que recebe uma lista com valores do mesmo tipo
# e devolve True se a lista está em ordem crescente e False caso contrário.

a = [1, 2,3,4,5,6,7,13,4]
b = [1,3,2,4]

def seq_crescente(a):

    k = 0

    while k < len(a)-1:

        if a[k] > a[(k+1)]:
            return False
        k = k + 1

    return True

print (seq_crescente(a))


