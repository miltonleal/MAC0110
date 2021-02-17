#Função multmatvet(a, b, n, m) que recebe a matriz a de n linhas por m colunas,
# o vetor b de m elementos. Devolve o vetor c de n elementos, resultado da multiplicação de a por b.

a = [[2,11,2,2,-1], [3,8,5,2,0], [-4,7,3,3,2], [3,4,-4,3,0]]
b = [3,7,5,3]

def mult_mat_vet(a,b,n,m):

    c = n*[0]

    for i in range(m):
        for j in range(n):
            c[j] = c[j] + a[i][j]*b[i]

    return c

print(mult_mat_vet(a,b,5,4))




