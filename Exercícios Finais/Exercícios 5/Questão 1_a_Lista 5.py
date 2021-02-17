#Escreva uma função LinhaZero(mat, lin) que recebe uma matriz mat e um int lin.
# Devolve True se todos os elementos da linha lin da matriz  mat forem iguais a 0 e False caso contrário.

mat = [[0,1],[0,0]]
lin = 1

def LinhaZero(mat,lin):

    linha_aux = len(mat[lin]) * [0] #cria uma lista com zeros do tamanho da linha
    if mat[lin] == linha_aux: #compara a linha com a lista com zeros
        return True
    return False

print(LinhaZero(mat,lin))
