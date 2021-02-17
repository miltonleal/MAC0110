
prod = {'13243564': [120, 5.43], '342549': [200, 1.25]}
cod = "342549"
quant = 20

def Update_Produto(prod,cod,quant):

    if not Get_Produto(prod,cod): ##caso o código do produto não exista
        return False

    if prod[cod][0] - quant >= 0: #realiza a subtração
        prod[cod][0] -= quant
        return True #se for possível a compra, retorna True
    return False #caso contrário

def Get_Produto(prod,cod):

    if cod in prod: #verifica se o código pertence ao dicionário produto
        return prod.get(cod) #retorna os valores associados à chave do cod
    return [] #retorna lista vazia, caso contrário

print(Update_Produto(prod,cod,quant))

