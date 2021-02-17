# Usando a função maior (x, y) definida no P11.3, escreva uma função maior3(x, y, z)
# que devolve o maior entre os 3 valores.

def main ():

    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    z = float(input("Digite o terceiro valor: "))

    print ("O maior número inserido é:", maior(x,y,z))

def maior (x, y, z):

    if x >= y  and x >= z: return x
    elif y >= x and y >= z: return y
    elif z >= x and z >= y: return z

main ()


