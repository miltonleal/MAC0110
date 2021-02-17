# Dados N, M > 0 calcular o Mínimo Múltiplo Comum entre N e M

def main():
 # leia N e M
    N = int(input("Entre com N: "))
    M = int(input("Entre com M: "))
 # primeiro candidata a mmc é o próprio N
    mmc = N

 # vamos testar todos os múltiplos de N
    while mmc % M != 0:
        mmc = mmc + N
 # imprimir o mmc
    print("O mmc entre", N, "e", M, "e' igual a", mmc)
main()