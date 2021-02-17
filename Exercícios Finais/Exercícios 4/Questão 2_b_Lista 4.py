def SemRepeticao(st):

    t = "" #inicia string vazia
    for i in st: #varre a string original
        if ProcuraChar(t, i): pass #se encontrar o caractere na string t, passa
        else: t += i #senão, adiciona o caractere à string t
    return t


def ProcuraChar(st, x):

    for i in range(len(st)):  # varre a string
        if x == st[i]:  # compara o caractere do parâmetro x com os caracteres da string
            return True
    return False

print (SemRepeticao("Eesccoola"))
