
p = [[5,20,4,20], [10,15,5,10], [15,30,2,30]]
q = [2,4,5,3]

def BuscaLoja(p,q):

    loja_mais_barata = [] #lista que contém a soma total das compras em cada loja

    for k in range(len(p)): #varre a lista p
        soma = 0 #inicia a soma e também zera a variável soma
        for i in range(len(q)): #varre a lista q
            soma += q[i]*p[k][i] #multiplica da qtd de produtos pelo preço da loja e soma
        loja_mais_barata.append(soma) #adiciona o total das compras de cada loja

        # imprime o resultado e ajusta o ordinal de cada loja para não começar em zero
        print ("O preço total dos",len(q),"produtos na loja", k+1,"é: R$",soma)

    #seleciona o valor mínimo total das compras de cada loja
    a = loja_mais_barata.index(min(loja_mais_barata)) + 1
    print ("A loja",a,"oferece o preço de compra mínimo")

    #cria lista para armazenar os preços mínimos de cada produto em cada loja
    lista_minimos = [len(p)*[0] for i in range(len(q))]

    for k in range(len(q)): #varre a lista de produtos
        for i in range(len(p)): #varre a lista de lojas
            lista_minimos[k][i] = q[k]*p[i][k] #multiplica o preço dos produtos e agrega à lista

    soma_minimos = 0 #variável que recebe o valor mínimo da compra percorrendo as lojas
    for j in range(len(lista_minimos)): #varre a lista de preços mínimos
        soma_minimos = soma_minimos + min(lista_minimos[j]) #soma os produtos com preços mínimos
    print ("O valor mínimo da compra percorrendo todas as lojas é: R$", soma_minimos)

BuscaLoja(p,q)







