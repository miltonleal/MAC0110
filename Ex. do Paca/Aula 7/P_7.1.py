#Dado n > 0 imprimir todos os divisores de n maiores que 1 e menores que n.

def main ():

#lê o número que será analisado
    n = int(input("Digite o valor do número que você deseja conhecer os divisores: "))

    #candidato a primeiro divisor
    div = 2

    #realiza o cálculo e a comparação
    while div <= n // 2:
        if n % div == 0:
            print (div, "é um divisor de", n)
        div = div + 1

main ()
