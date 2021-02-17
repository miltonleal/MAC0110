
#a = [0,8,9,7,3,9,7,4]

a = [4,7,9,3,7,9,8,0]

def Bolha(a):
    n = len(a)
    # i = 1, 2, ..., n – 1 (do segundo até o último)
    for i in range(1, n):
    # sobe com a[i] até encontrar o lugar adequado
        j = i
        while j > 0 and a[j] < a[j - 1]:
        # troca com o seu vizinho
            a[j], a[j - 1] = a[j - 1], a[j]
            print (1)
            # continua subindo
            j = j - 1

    return a

print (Bolha(a))