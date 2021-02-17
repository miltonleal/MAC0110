# Dado n > 0 calcular os divisores de n maiores que 1 e menores que n

def main ():

    n = int(input("Digite o número que você deseja conhecer os divisores: "))

    div = 2

    for div in range (2, n//2 + 1):
        if n % div == 0:
            print (div, "é um divisor de", n)

main ()




