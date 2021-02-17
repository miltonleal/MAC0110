#Função retira_primos(list_num) que recebe uma lista de inteiros positivos
# e retira dela todos os primos, devolvendo o resultado numa nova lista.

a = [2,3,4,5,6,7,8,9,10,11,12,13]

def retira_primos(a):

    lista_aux = [] + a
    nova_lista = []

    for i in range(len(lista_aux)):
        if primo(lista_aux[i]): pass
        else: nova_lista.append(lista_aux[i])

    return nova_lista

def primo(x):

    div = 2
    lista = []

    while div * div <= x:

        if x % div == 0:
            return False
        div = div + 1
    return True

print(retira_primos(a))