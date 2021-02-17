#  Dado N > 0, inteiro, calcular a soma N + N/2 + N/4 + ... + 1
#  solução abaixo considera a divisão inteira. Por exemplo, para N = 15 (15 + 7 + 3 + 1), para N = 10
# (10 + 5 + 2 + 1).

def main():

    N = int(input("Entre com N > 0 e inteiro:"))
    soma = 0
    while N > 0:
        soma = soma + N
        N = N // 2
    print("Valor da soma = ", soma)

main()