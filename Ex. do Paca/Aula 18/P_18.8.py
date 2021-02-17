#Função multmatmat(a, b, n, m, p) que recebe a matriz a n x m, b m x p.
# Devolve matriz n x p, resultado da multiplicação da matriz a pela matriz b.

a = [[1,2,3], [1,1,1]]
b = [[1,2],[2,1],[3,1]]


def mult_mat_mat(a,b,n,m,p):

    c = [p*[0] for i in range(n)]

    for i in range (n):
        for j in range (p):
            for k in range (m):
                c[j][i] = c[j][i] + a[k][i] * b[j][k]

    return c

print(mult_mat_mat(a,b,3,2,3))




