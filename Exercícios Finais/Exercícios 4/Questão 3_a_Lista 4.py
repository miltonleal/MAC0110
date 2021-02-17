#Escreva uma função ContaString(st, sx) que devolve o número de vezes que a string sx
# ocorre dentro da string st.


def ContaString(st,sx):

    contador = 0 #inicia o contador
    for i in range(len(st)): #varre a string maior
        if st[i:i + len(sx)] == sx: #verifica se a substring está na string maior
            contador += 1 #adiciona ao contador em caso positivo
    return contador

print (ContaString("o rato roeu a roupa do rei de roma", "ratoeira"))