# P8.1) Dados x float e N > 0 inteiro, imprimir uma tabela com os valores de x, x2, x3
def main ():


    x = float(input("Insira um número: "))
    N = int(input("Insira o expoente: "))

    cont = 1


    print("expoente    potência")
    while cont <= N:

        print ("   %03d %13.5f" % (cont, x**cont))
        cont = cont + 1
main ()



