#Função somamat(a, b, n, m) que recebe as matrizes a e b de n linhas por m colunas.
# Devolve matriz também n x m que é a soma de a com b.

a = [[0,0], [0,1]]
b=  [[0,2], [2,1]]

def soma_mat(a,b,m,n):

    c = [m*[0] for i in range (n)]

    for i in range (n):
        for j in range (m):
            c[i][j] = a[i][j] + b[i][j]
    return c

print (soma_mat(a,b,2,2))


for i in range(len(a)):
    print()
    for j in range(len(a)):
        print("%8.2f"%a[i][j], end = "")