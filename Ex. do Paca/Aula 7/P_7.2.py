# Dado n > 1, inteiro, verificar se n é primo

def main ():

    #leia n
    n = int(input("Digite o número que você deseja verificar se é primo: "))

    div = 2

    #
    while div <= n // 2:
        if n %  div == 0:
            print (div, "é um divisor de", n, ", portanto, não é primo")
            return
        div = div + 1

    print (n, "é um número primo")

main ()
