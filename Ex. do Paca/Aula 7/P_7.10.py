# Dados N, M > 0 calcular o Mínimo Múltiplo Comum entre N e M
# escolher o maior e o menor entre N e M e testar somente os múltiplos do maior

def main():
 # leia N e M
    N = int(input("Entre com N: "))
    M = int(input("Entre com M: "))

 # compara os números e define candidato para mmc
    if N >= M:
        mmc = N
        mmc_menor = M
    else:
        mmc = M
        mmc_menor = N

 # realiza a verificação de qual número é o mmc
    while mmc % mmc_menor != 0:
        mmc = mmc + mmc
    print ("O mmc entre", N, "e", M, "é:", mmc)

main ()


