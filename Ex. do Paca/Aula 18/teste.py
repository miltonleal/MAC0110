
n = int(input("Digite o número de linhas: "))

m = int(input("Digite o número de colunas: "))

mat = []

for i in range (n):
    mat.append(m*[0])
    for j in range (m):
        mat [i][j] = float(input("Digite o valor do elemento: "))

for i in range(n):
    print()
    for j in range(m):
        print("%8.2f"%mat[i][j], end = "")

for i in range(n):
    print()
    nz = 0
    for j in range(m):
        if mat[i][j] == 0: nz = nz + 1
    print("Linha ", i, "com ", nz, "zeros")

for i in range (n):
    print ()
    x = mat [i][0]
    maior, menor, soma = x, x, x
    for j in range (1,m):
        if mat [i][j] > maior: maior = mat[i][j]
        if mat [i][j] < menor: menor = mat[i][j]
        soma = soma + mat[i][j]
    print ("Linha", i, "maior = ", maior, "menor = ", menor, "media = ", soma/m)

for k in range (m):
    print ()
    x = mat [0][k]
    maior, menor, soma = x, x, x
    for p in range (1,n):
        if mat [p][k] > maior: maior = mat[p][k]
        if mat [p][k] < menor: menor = mat[p][k]
        soma = soma + mat[p][k]
    print ("Coluna", k, "maior =", maior, "menor = ", menor, "media = ", soma/n)
