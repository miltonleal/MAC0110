#Escreva uma função recursiva Potencia(x, n) que recebe x ≠ 0 float e n ≥ 0 int. Devolve xn

def Potencia(x,n):

    if n == 0: return 1 #caso base
    return x*Potencia(x, n-1) #multiplica n vezes o x pelo próprio x

print(Potencia(0,10))
