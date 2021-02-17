# Dado n > 0 inteiro, imprimir o gráfico da função x2 – x + 1 para x = -n até n.
# Imprimir o gráfico usando como ordenadas o eixo horizontal e como abscissas o eixo vertical.

def main ():

    # ler n inteiro >= 0
    n = int(input("Entre com o valor de n inteiro >= a zero: "))

    # Variar k de -n até n e
    # para cada k imprimir uma nova linha do gráfico
    for k in range (-n, n+1):
        print ("%5d" %k, end = '')
        # valor da função em k
        f = k * k - k + 1
        # imprimir f vezes '.' e em seguida '*'
        for j in range(f): print('.', end='')
        print('*')

main ()

