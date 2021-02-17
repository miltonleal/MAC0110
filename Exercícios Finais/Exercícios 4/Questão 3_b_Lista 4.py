#Escreva uma função MaiorSubString(s1, s2) que devolve uma string com o maior prefixo de s2 que
# ocorre dentro da string s1. Use obrigatoriamente a função ContaString acima.

s1 = "O rato sai caro pato"
s2 = "pato rato"


def MaiorSubString(s1,s2):

    tamanho_substring = len(s2) #determina o tamanho da substring
    while ContaString(s1,s2[0:tamanho_substring]) == 0: #compara a substring com a string maior
        tamanho_substring -= 1 #se não encontrou a substring na string maior, reduz o tamanho da substring
    return s2[0:tamanho_substring] #retorna o maior prefixo

def ContaString(st,sx):

    contador = 0 #inicia o contador
    for i in range(len(st)): #varre a string maior
        if st[i:i + len(sx)] == sx: #verifica se a substring está na string maior
            contador += 1 #adiciona ao contador em caso positivo
    return contador

print (MaiorSubString(s1,s2))