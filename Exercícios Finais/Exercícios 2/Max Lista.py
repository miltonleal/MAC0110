#Escreva uma função MaxLista(A, K) que recebe como parâmetros, uma lista A e um inteiro K ≥ 0
# e devolve o índice do elemento máximo entre A[0], A[1], ..., A[K]

A= [100,11,3,10,5,6,798,7,8,9]

K = 9

def MaxLista(A,K):

    indmax = 0

    for j in range (1, K+1):
        if A[indmax] < A[j]: indmax = j

    return indmax

print (MaxLista(A,K))

