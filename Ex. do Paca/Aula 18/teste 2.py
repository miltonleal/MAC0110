def verifica_linhas(a):

    subs = [len(a)*[0] for i in range (len(a))]

    for i in range (len(a)):
        for j in range (len(a)):
            subs[i][j] = a[j][i]

    for j in range (len(a)):
        if subs[j] not in subs[j+1:]:
            linhas_iguais = False
        else:
            linhas_iguais = True
            break

    return linhas_iguais

print(verifica_linhas(a))
