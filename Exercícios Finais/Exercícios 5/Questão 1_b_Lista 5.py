#Escreva uma função ColunaZero(mat, col) que recebe uma matriz mat e um int col.
# Devolve True se todos os elementos da coluna col da matriz  mat forem iguais a 0 e False caso contrário.

mat =[[0,2,0,6,0], [0,3,5,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,1,2,0,0], [0,0,0,0,0]]
col = 0

def ColunaZero(mat,col):

    for i in range (len(mat)): #varre as colunas
        if mat[i][col] != 0: #compara os elementos da coluna com o zero
            return False
    return True

print(ColunaZero(mat,col))
