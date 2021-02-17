#Função ind_min_col (a, n, col) que receba a matriz a de n x n elementos
# e devolve como resultado o índice do menor elemento da coluna col desta matriz

a = [[1,8], [8,6]]

def ind_min_col(a,col):

    indmin = 0

    for i in range (1,len(a)):
        if a[i][col] < a[indmin][col]: indmin = i
    return indmin

print (ind_min_col(a,1))




