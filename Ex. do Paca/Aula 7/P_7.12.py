#  Dados N e M > 0 calcular o Máximo Divisor Comum entre N e M, usando o algoritmo acima.

def main():
     # leia N e M
     N = int(input("Entre com N: "))
     M = int(input("Entre com M: "))
     # determina o menor deles
     if N < M: k = N
     else: k = M

     # repetição até encontrar um divisor de ambos
     while N % k != 0 or M % k != 0:
        k = k - 1

     # imprimir o mdc
     print("O mdc entre", N, "e", M, "é igual a", k)
main()