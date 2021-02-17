

n = int(input("digite n: "))

def primo (x):

    div = 2

    lista = []

    while div * div <= x:

        if x % div == 0:
            return False
        div = div + 1
    return True

def primos_ate(n):

    pri = []
    for k in range (2,n+1):

        if primo(k): pri.append(k)
    return pri

print (primos_ate(n))
