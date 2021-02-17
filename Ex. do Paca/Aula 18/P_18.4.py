# Idem, verificando se a é uma matriz diagonal. Uma matriz é diagonal
# se todos os elementos fora da diagonal principal são nulos.

a = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]


def mat_diagonal(a,n):

    for i in range(n):
        for j in range (i):
            if a[i][j] != a[j][i]:
                return False

    if a[i][j] == 0:
        return True

print (mat_diagonal(a,4))


