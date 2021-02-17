#verificando se é uma matriz identidade.
# Uma matriz é identidade quando é diagonal e todos os elementos da diagonal principal são iguais a 1.

a = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

def mat_identidade(a,n):

    for i in range(n):
        if a[i][i] == 1: pass
        else: return False

        for j in range (i):
            if a[i][j] != a[j][i]:
                return False

    if a[i][j] == 0:
        return True

print (mat_identidade(a,4))


for i in range(len(a)):
    print()
    for j in range(len(a)):
        print("%8.2f"%a[i][j], end = "")

