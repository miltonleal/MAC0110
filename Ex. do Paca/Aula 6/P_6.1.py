# Dado N > 0 e uma sequência de N números, determinar o maior elemento da sequência.

def main():
    # ler a quantidade de números N
    N = int(input("Digite a quantidade de números da sequência: "))

    # Consistência dos dados de entrada
    if N == 0:
        print("A sequência possui zero elementos")
    else:
        maior = float(input("Digite o primeiro valor da sequência: "))

    # inicia o contador e define o maior número inicial
        contador = 1

    # repete a comparação dos valores imputados N vezes
        while N - 1 >= contador:
            #ler o próximo
            x = float(input("Digite o próximo valor da sequência: "))
            #faz a comparação
            if x > maior: maior = x
            contador = contador + 1
        #imprime o resultado
        print ("O maior valor da sequência é:", maior)
main()
