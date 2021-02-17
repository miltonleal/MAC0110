#Escreva uma função GeraTransposta(A) que recebe uma matriz quadrada A e
# devolve a correspondente matriz transposta.

A = [[1, 2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

def GeraTransposta(A):

    T = [len(A)*[0] for i in range(len(A))] #cria lista zerada tamanho nxn

    for i in range(len(A)): #varre a matriz
        for k in range(len(A)): #varre a matriz
            T[i][k] = A[k][i] #realiza a transposição dos elementos
    return T

print(GeraTransposta(A))