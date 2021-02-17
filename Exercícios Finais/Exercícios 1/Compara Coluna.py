#Escreva uma função ComparaCol(MAT, C1, C2, N) que verifica
# se os N elementos das colunas C1 e C2 são iguais, devolvendo True ou False.

MAT = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 2]]



def compara_colunas(MAT, C1, C2, N):

    for j in range(N):
        if MAT[j][C1] != MAT[j][C2]:
            return False
            break
    return True

print(compara_colunas(MAT, 0, 2, 4))
