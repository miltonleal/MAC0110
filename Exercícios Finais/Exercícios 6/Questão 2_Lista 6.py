def LeiaMatriz(NomeArq):

    mat = {} #cria o dicionário
    arq = open(NomeArq, "r") #abre o arquivo

    for linha in arq: #varre as linhas do arquivo
        lin = linha[:len(linha) - 1] #tira o \n do final
        v = lin.split('\t')#separa os elementos
        #adiciona os dados ao dicionário
        mat.update({str(v[1]):([int(v[0]), int(v[2]), int(v[3]),
                                int(v[4]), int(v[5]), int(v[6]), int(v[7])])})

    arq.close()
    return mat

print(LeiaMatriz("megasenac.txt"))