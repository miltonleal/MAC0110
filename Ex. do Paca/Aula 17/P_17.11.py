#Função procura_elemento(a, x), que procura elemento igual a x na lista a,
# devolvendo como o índice do primeiro elemento que é igual a x ou -1 caso não encontre.
# É quase a mesma coisa que a função index(x) já usada anteriormente. Assim, suponha que não exista a index(x)

a = [0,0,0,0,1,1,1,1,2,2,2]

def procura_elemento(a,x):

    for k in range (len(a)):
        if a[k] == x:
            return k

    else: return -1

print (procura_elemento(a,3))


