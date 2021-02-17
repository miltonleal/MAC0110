#Função contem(a, b) que devolve True a contém b e False se não

def contem(a,b):

    for i in range (len(b)):

        if b[i] in a: pass
        else: return False
    return True

a = [1,2,3,4,5]
b = [1,2,7,4,5,6,7,8,5,5,7,8]

print (contem(a,b))

