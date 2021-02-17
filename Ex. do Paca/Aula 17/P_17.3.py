#Função troca_valor(a, x, y) que substitui todos os elementos da lista a iguais a x por y.

def troca_valor (a,x,y):

    for t in range (len(a)):
        if a[t] == x:
            a[t] = y


a = [1,2,1,2,1,2]

troca_valor(a,1,2)

print (a)

j = ["branco", "azul", "amarelo", "verde", "branco"]

troca_valor(j, "branco", "verde")

print (j)





