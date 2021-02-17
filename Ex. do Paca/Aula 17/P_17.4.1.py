#elimina zeros

def elimina_zeros(a):

    k = 0

    while k < len(a):
            if a[k] == 0: del a[k]
            else: k +=1


x = [0,1,2,3,0,4,0,5,0]
elimina_zeros(x)

print (x)
