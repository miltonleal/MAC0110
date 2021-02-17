#Função repetidos(a) que devolve True se a lista a tem elementos repetidos e False caso contrário.

a = [0,1,3,5,6,7,8]

def repetidos(a):

    k = 0

    while k < len(a):
        if a[k] in a[k+1:]:
            return True
        else:
            k = k +1
    return False

print (repetidos(a))