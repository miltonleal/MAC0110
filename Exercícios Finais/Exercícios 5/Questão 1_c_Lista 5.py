#Escreva a função void LCZero(mat) que devolve uma dupla de listas.
# A primeira com todas as linhas zeradas e a segunda com todas as colunas zeradas da matriz mat.
# Exemplo – se mat for a matriz abaixo, devolve: ([2, 3, 5], [0, 4])

mat =[[0,2,0,6], [0,3,5,0], [0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]


def LCZero(mat):

    a,b = [],[] #cria duas listas vazias
    tupla = (a,b) #cria a tupla com as listas vazias

    for i in range(len(mat)): #varre as linhas
        if LinhaZero(mat,i): #verifica se as linhas estão zeradas
            a.append(i) #se sim, adiciona na lista das linhas

    for k in range(len(mat[0])): #varre as colunas
        if ColunaZero(mat,k): #verifica se as colunas estão zeradas
            b.append(k) #se sim, adiciona na lista das colunas

    return tupla

def ColunaZero(mat,col):

    for i in range (len(mat)): #varre as colunas
        if mat[i][col] != 0: #compara os elementos da coluna com o zero
            return False
    return True


def LinhaZero(mat, lin):
    linha_aux = len(mat[lin]) * [0]  # cria uma lista com zeros do tamanho da linha
    if mat[lin] == linha_aux:  # compara a linha com a lista com zeros
        return True
    return False

print (LCZero(mat))
