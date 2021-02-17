#Escreva uma função Ordem(A) que recebe como parâmetros, uma lista A e classifica os elementos da lista A em ordem crescente, usando o algoritmo da seleção.
# Use obrigatoriamente a função MaxLista acima para selecionar o maior.
# Algoritmo da Seleção: Para i = n-1, n-2,..., 1 selecione o maior até a[i] e troque com a[i].

A= [9,1,3,5,2,6,8,2,4]


def Ordem(A):

    for i in range(len(A)-1):
        imax = MaxLista(A, i)
        for j in range(i+1, len(A)):
            if (A[imax] > A[j]): imax = j
        A[i], A[imax] = A[imax], A[i]
    return A

def MaxLista(A, K):

    indmax = 0
    for j in range (1, K+1):
        if A[indmax] < A[j]: indmax = j
    return indmax

print (Ordem(A))







