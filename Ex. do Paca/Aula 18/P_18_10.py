#Função verifica_linhas(a, n) que verifica se a matriz a n x n, possui 2 colunas iguais, devolvendo True ou False.

a = [[1,0,0], [0,1,1],[1,1,0]]


def verifica_colunas(a):

    subs = [len(a)*[0] for i in range (len(a))]

    for i in range (len(a)):
        for j in range (len(a)):
            subs[i][j] = a[j][i]

    for j in range (len(a)):
        if subs[j] not in subs[j+1:]:
            colunas_iguais = False
        else:
            colunas_iguais = True
            break

    return colunas_iguais

print(verifica_colunas(a))


