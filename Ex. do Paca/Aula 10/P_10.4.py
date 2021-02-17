#  Dado n ≥ 0 calcular n!

def main ():

    n = int(input("Digite o número que você deseja calcular a multiplicação fatorial: "))

    fat = 1

    for i in range (2, n+1): fat *= i

    print ("O valor de %d! é =" %n, fat)

main ()
main ()


