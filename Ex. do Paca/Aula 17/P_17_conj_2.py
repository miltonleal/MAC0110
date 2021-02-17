#Função pertence(a, x) que devolve True se o elemento x pertence ao conjunto a e False se não.

a = [1,2,3,4,5]

def pertence(a,x):

    for i in range (len(a)):

        if x in a[i:]: return True
        else: return False

print (pertence(a,3))


