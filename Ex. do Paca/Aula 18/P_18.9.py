#Função verifica_linhas(a, n) que verifica se a matriz a n x n, possui 2 linhas iguais, devolvendo True ou False.

a = [[1,1,0,1], [1,2,0,1],[3,3,0,0], [3,3,0,0]]

def verifica_linhas(a):

    for j in range (len(a)):
        if a[j] not in a[j+1:]:
            linhas_iguais = False
        else:
            linhas_iguais = True
            break

    return linhas_iguais

print(verifica_linhas(a))



