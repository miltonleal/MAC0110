#Dado n > 0 inteiro, calcular o valor de x.y.z para x, y, z = 0, 1, 2, ... , n.
# Nesse caso terá 3 níveis de repetição.

def main ():

    n = int(input("Insira o valor de n: "))

    print ("    x    y    z     valor")

    for x in range (1, n+1):
        for y in range (1, n+1):
            for z in range (1,n+1): print ("%5d%5d%5d%8d" % (x, y, z, (x*y*z)))

main ()