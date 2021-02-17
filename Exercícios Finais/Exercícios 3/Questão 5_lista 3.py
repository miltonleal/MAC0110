#Escreva uma função recursiva Maiores(L, x) que recebe uma lista L e um valor x.
# Devolve quantos elementos de L são maiores que x.

def Maiores(L,x):

    if L == []: return 0 #caso base
    if L[len(L)-1] > x: #compara o último elemento com x
        return 1 + (Maiores(L[:len(L)-1], x)) #soma 1 e chama a função ajustando o elemento de comparação
    return 0 + (Maiores(L[:len(L)-1], x)) #soma 0 e chama a função ajustando o elemento de comparação

print (Maiores([5,4,6], 3))

