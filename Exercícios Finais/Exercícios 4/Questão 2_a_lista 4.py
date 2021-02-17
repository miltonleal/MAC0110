#Escreva uma função ProcuraChar (st, x) que procura o caractere x dentro do string st,
# devolvendo True ou False.

def ProcuraChar (st,x):

    for i in range (len(st)): #varre a string
        if x == st[i]: #compara o caractere do parâmetro x com os caracteres da string
            return True
    return False

print (ProcuraChar("", "a"))
