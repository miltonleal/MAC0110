def Criptografa(st,dsl):

    cripto_string = "" #cria string vazia

    for i in st: #varre a string
        cripto_string += chr((ord(i) + dsl) % 256) #desloca a tabela ASCII com soma circular
    return cripto_string

print (Criptografa("Milton", 70))