a = [2, 5, 27, 36, 73, 92, 97, 101, 123, 147, 169, 191, 199]


n = 13

x = 85

def busca_binaria(a, n, x):
    inicio, fim = 0, n - 1
    # procura enquanto há algum elemento na tabela
    while inicio <= fim:
        meio = (inicio + fim) // 2
        print ("meio = ", a[meio])

    # compara com o elemento médio
        if x == a[meio]: return meio
        print(1)
    # redimensiona a tabela
        if x > a[meio]: inicio = meio + 1
        else: fim = meio - 1
    # saiu do while sem encontrar
    return -1

print (busca_binaria(a,n,x))