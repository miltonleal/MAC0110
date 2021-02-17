#Função conta_elementos(a, x) que devolve quantas vezes o elemento x ocorre na lista a.
# É exatamente o que faz a função count() que já usamos.
# Suponha então que a função count() não exista e construa essa função.

def conta_elementos(a,x):

    cont = 0

    for k in range(len(a)):
        if a[k] == x:
            cont = cont + 1
    return cont


a = [0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4]

print (conta_elementos(a, 2))


