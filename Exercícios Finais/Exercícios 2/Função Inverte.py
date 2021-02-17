L = [4,2,6,4,5,6,4]

def Inverte(L):

    for j in range (-1, -(len(L) +1), -1):
        L.append(L[j])
        del L[j-1]
    return L

print (Inverte(L))

