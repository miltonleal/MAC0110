#Função contido(a, b) que devolve True a está contido em b e False se não

def contido(a,b):

    for i in range (len(a)):

        if a[i] in b: pass
        else: return False
    return True

a = [1,2,3,4,5,13]
b = [1,2,3,7,4,5,6,7,8,5,5,7,8]

print(contido(a,b))


