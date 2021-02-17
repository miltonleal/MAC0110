#dado n > 1, inteiro, verificar se n é primo
#não precisa testar para todos os possíveis divisores de 1 em 1. Basta testar para 2 e depois só os ímpares

def main ():

    #leia n
    n = int(input("Type a number you'd like to check if is prime or not: "))

    div = 2
    cont = 3

    if n % 2 == 0:
        print (n, "is not prime number.")
        return

    while cont <= n // 2:
        if n % cont == 0:
            print (n, "is not prime number.")
            return
        cont = cont + 2

    print(n, "is a prime number.")


main ()
