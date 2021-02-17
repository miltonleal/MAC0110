#Função mult_pol(a, b) que devolve lista contendo o produto dos polinômios a e b

a = [1,1,3,4]
b = [2,2]

def mult_pol(a,b):

    res = [0]*(len(a)+len(b)-1) #cria o tamanho do polinomio resultante
    for c1,i1 in enumerate(a): #o c1 serve como base pra saber o indice do X, o i1 é o elemento que vai ser multiplicado
        for c2,i2 in enumerate(b): #o c2 serve como base pra saber o indice do X, o i2 é o elemento que vai ser multiplicado
            res[c1+c2] += i1*i2 #c1+c2 = indice do X / i1*i2 é a multiplicação dos elementos
    return res

print (mult_pol(a,b))

