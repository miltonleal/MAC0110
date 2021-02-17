#Função troca_listas(a, b) que troca os valores entre as listas a e b.
# Se as listas não tiverem o mesmo tamanho devolve False, senão True.

def troca_listas(a,b):

    if len(a) != len(b): return False
    for t in range (len (a)):
        a[t], b[t] = b[t], a[t]
    return True

x = [1,2,3,4,5]

y = [2,3,56,5,4,6]

z = [1,2,3]


if troca_listas(x,y):
    print (x)
    print (y)
else: print("diferente")

