# Função simetrica(a, n) que verifica se a matriz a de n linhas e n colunas é uma matriz simétrica,
# isto é, se a[i][j] é igual a a[j][i], devolvendo True (sim) ou False (não). percorrendo apenas o triângulo inferior

a = [[2,4,4], [4,6,6], [4,6,9]]


def simetrica(a,n):
    for i in range(n):
        print("i = ", i)
        for j in range(i):
            print("i =", i,"j = ",j)
            if a[i][j] != a[j][i]:
                return False
    return True

print(simetrica(a, 3))


for i in range(len(a)):
    print()
    for j in range(len(a)):
        print("%8.2f"%a[i][j], end = "")