#Calcular os valores da função x2 - y2 + xy para x e y = -10, -9, ..., 9, 10.

def main ():

    print ("%4s%6s%10s" % ("x","y","função"))
    print ()
    for x in range (-10,11):
        for y in range (-10,11): print ("%5d %5d %6d" % (x, y, ((x*x) - (y*y) + (x*y))))

main ()
