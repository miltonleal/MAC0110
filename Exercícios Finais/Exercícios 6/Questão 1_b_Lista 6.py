
prod = {'13243564': [120, 5.43], '342549': [200, 1.25]}
cod = '342549'

def Get_Produto(prod,cod):

    if cod in prod: #verifica se o código pertence ao dicionário produto
        return prod.get(cod) #retorna os valores associados à chave do cod
    return [] #retorna lista vazia, caso contrário

print(Get_Produto(prod,cod))
