def main (nome_arquivo):

    dicionario = Produto_Dic(nome_arquivo) #cria o dicionário
    dicionario_aux = Produto_Dic(nome_arquivo) #cria o mesmo dicionário auxiliar

    while True: #loop geral
        cod = str(input("Digite o valor do código: ")) #requisita o código do produto
        if cod == '0': #se o código é zero, sai do loop
            break
        if Get_Produto(dicionario, cod): #se o código existe, continua
            pass
        else: #caso o código não exista, solicita novo código
            print("Código não encontrado. Por favor, reinsira o código.")
            continue

        while True: #loop para quantidade
            quant = int(input("Digite a quantidade de produtos: ")) #requisita qtd
            if Update_Produto(dicionario, cod, quant): #se existe estoque, atualiza
                break #retoma o loop anterior
            #caso contrário, solicita nova quantidade
            else: print("A quantidade excede o estoque. Por favor, reinsira a quantidade.")
        continue

    print("Relatório de compras")
    print("Código do produto - Quantidade comprada")
    for k in dicionario.keys(): #varre o dicionário
        # subtrai a qtd inicial da qtd comprada
        print("%12s%19s" % (k,dicionario_aux[k][0] - dicionario[k][0]))

def Update_Produto(prod,cod,quant):

    if cod not in prod: #caso o produto seja inexistente
        return False

    if (prod[cod][0] - quant) >= 0: #realiza a comparação para saber se há estoque
        prod[cod][0] -= quant #realiza a subtração do estoque
        return True #se for possível a compra, retorna True
    return False #caso contrário


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


def Get_Produto(prod,cod):

    if cod in prod: #verifica se o código pertence ao dicionário produto
        return prod.get(cod) #retorna os valores associados à chave do cod
    return [] #retorna lista vazia, caso contrário

main("produtos.txt")
