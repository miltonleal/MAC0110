# Escreva a função VerificaLC(MAT, N, M) que verifica se a matriz MAT de N linhas por M colunas
# possui 2 linhas ou 2 colunas iguais, devolvendo True ou False.

MAT = [[1, 1, 3], [1, 2, 3], [1, 4, 3], [2, 1, 3]]


def VerificaLC(MAT, N, M):

    for j in range(N):
        for k in range(j + 1, N):
            if compara_linhas(MAT, j, k, M) == True:
                return True
                break

        for i in range(M - 1):
            for j in range(1, M):
                if compara_colunas(MAT, i, j, N) == True:
                    return True
    return False

def compara_colunas(mat, C1, C2, N):

    for j in range(N):
        if mat[j][C1] != mat[j][C2]:
            return False
            break
    return True

def compara_linhas(mat, L1, L2, m):

    if mat[L1] == mat[L2]:
        return True
    else: return False

print(VerificaLC(MAT, 4, 2))

