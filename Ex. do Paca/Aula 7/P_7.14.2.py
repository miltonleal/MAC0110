#  Dado N > 0, inteiro, calcular a soma N + N/2 + N/4 + ... + 1
#  solução abaixo considera a divisão não inteira. Para N = 15 (15 + 7.5 + 3.75 + ...)

def main():
     N = int(input("Entre com N > 0 e inteiro:"))
     soma = 0
     while N > 0:
        soma = soma + N
        N = N / 2
     print("Valor da soma = ", soma)
main()