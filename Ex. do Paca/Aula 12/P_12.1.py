# Dado n e p inteiros, n, p ≥ 0, calcular as combinações de n elementos p a p, isto é: n! / (p! * (n - p)!).

def main ():

    # ler n e p
    n = int(input("Entre com n maior ou igual a zero:"))
    p = int(input("Entre com p maior ou igual a zero:"))

    # imprime o número de combinações de n p a p
    print("Combinações = %d" % (fat(n) / (fat(p) * fat(n - p))))

def fat(k):
    f = 1
    for i in range (2, k+1): f = f*i
    return f



main ()

