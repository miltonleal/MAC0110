#Escreva uma função DesCriptografa(st, dsl) que faz o inverso.
# Devolve st devidamente descriptografada com deslocamento dsl.

def DesCriptografa (st,dsl):

    string_decrypt = "" #cria string vazia

    for i in st:  #varre a string
        string_decrypt += chr((ord(i) + (-dsl)) % 256)  #desloca a tabela ASCII no sentido inverso
    return string_decrypt

print (DesCriptografa("ÿ",255))