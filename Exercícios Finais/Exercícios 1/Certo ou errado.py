a = [1,2,4,3,5]


def Ordem(a, n):
    i = 0
    while i < n -1 and a[i] <= a[i + 1]: i = i + 1
    if i == n - 1: return True
    return False




print (Ordem(a, 5))



