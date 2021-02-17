

def Produto_Dic(nome_arquivo):

    #abre o arquivo e elimina os \n
    arquivo = [line.rstrip() for line in open(nome_arquivo)]
    dicionario = {} #cria um dicionário vazio

    for i in arquivo: #varre o arquivo
        itens = i.split(",") #separa os itens
        #adiciona ao dicionário
        dicionario.update({str(itens[0]):([(int(itens[1])), (float(itens[2]))])})
    return dicionario

    arquivo.close()

print(Produto_Dic("produtos.txt"))
