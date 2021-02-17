#  Dados N e M > 0 calcular o Máximo Divisor Comum entre N e M

def main():
    # leia N e M
    N = int(input("Entre com N: "))
    M = int(input("Entre com M: "))

    # repetição até encontrar resto zero
    while N % M != 0:
    # troca os valores de N e M
        N, M = M, N % M
    # O mdc e' o M
    print("O mdc é", M)

main()