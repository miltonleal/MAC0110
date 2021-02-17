# Dado n e m maiores que zero e inteiros, imprimir uma tabela com os valores de x*y
# para x=1, 2, ..., n e y=1, 2, ... , m *usar função while

def main():
    # ler n e m inteiros >= 0
    n = int(input("Entre com o valor de n inteiro >= 0: "))
    m = int(input("Entre com o valor de m inteiro >= 0: "))

    # inicializa contadores
    cont_m = 1
    cont_n = 1
    cont_mx = 1
    cont_nx = 1

    # imprimir a linha de cabeçalho
    print("     ", end='')
    while cont_m <= m:
        print("%5d" % cont_m, end='')
        cont_m = cont_m + 1
    print()

    # varia n de 1 até n e multiplica contador auxiliar de m por contador auxiliar de n
    while cont_n <= n:
        print("%5d" % cont_n, end='')
        while cont_mx <= m:
            print("%5d" % (cont_mx * cont_n), end='')
            cont_mx += 1
        cont_n += 1
        cont_mx = 1
        print()
        continue
    print()


while True:
    main()


