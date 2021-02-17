# Função simetrica(a, n) que verifica se a matriz a de n linhas e n colunas é uma matriz simétrica,
# isto é, se a[i][j] é igual a a[j][i], devolvendo True (sim) ou False (não).

a = [[2,4,4], [4,6,6], [4,6,9]]


def simetrica(a,n):
    for i in range(n):
        print("i = ", i)
        for j in range(n):
            print("i =", i,"j = ",j)
            if a[i][j] != a[j][i]:
                return False
    return True

print(simetrica(a, 3))
