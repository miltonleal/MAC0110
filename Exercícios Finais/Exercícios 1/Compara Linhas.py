# Escreva uma função ComparaLin(Mat, L1, L2, M) que verifica se
# os M elementos das linhas L1 e L2 são iguais, devolvendo True ou False

Mat = [[1, 1, 0], [1, 1, 0], [3, 2, 0], [3, 3, 0]]

L1 = 0
L2 = 3
M = 3


def compara_linhas(Mat, L1, L2, M):

    if Mat[L1] == Mat[L2]:
        return True
    else: return False

print(compara_linhas(Mat, L1, L2, M))

