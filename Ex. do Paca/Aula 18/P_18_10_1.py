'''
 Faça um programa que dados n e m, uma matriz de preços de n x m elementos, que são os preços
de m produtos em n lojas, e também um vetor de m elementos que são as quantidades de cada um dos m
produtos que serão compradas, determine:
- O valor total da compra em cada loja (use a função multmatvet)
- Qual a loja que têm o valor mínimo para a compra e qual esse valor.
- O preço mínimo de cada produto e qual das n lojas tem esse preço mínimo (use a função
ind_min_col)
- O valor da compra, se usado o preço mínimo de cada produto (use a função ind_min_col)
'''

n = int(input("Digite o número de lojas: "))

m = int(input("Digite o número de produtos: "))




matriz_precos = [m*[0] for i in range (n)]

vetor_quantidade = [m*[0]]

for i in range (n):
    for j in range (m):
        matriz_precos[i][j] = float(input("Digite o preço do produto: "))

for k in range (m):
    vetor_quantidade[k] = float(input("Digite a quantidade de cada produto: "))

### valor total

def mult_mat_vet(matriz_precos,vetor_quantidade,n,m):

    c = n*[0]

    for i in range(m):
        for j in range(n):
            c[j] = c[j] + matriz_precos[i][j]*vetor_quantidade[i]

    return c

print("O valor total é:", mult_mat_vet(matriz_precos,vetor_quantidade,n,m))

### valor minimo por loja

def val_min_col(matriz_precos,m):

    cont = 0
    lista_valmin = []

    while cont < m:

        valmin = matriz_precos[0][cont]

        for i in range (1,len(matriz_precos)):
                if matriz_precos[i][m] < matriz_precos[valmin][m]:
                    lista_valmin.append(matriz_precos[i][m])
        cont = cont + 1
    return lista_valmin

print ("O valor mínimo por loja é:", val_min_col(matriz_precos,m))


