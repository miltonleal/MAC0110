#Dado N > 0 e uma sequência de N números, determinar o maior elemento da sequência, o menor elemento e a média

def main():
    #lê a quantidade de elementos da sequência
    N = int(input("Digite o número de elementos da sequência: "))

    #consistência dos dados de entrada
    if N == 0:
        print ("Esta sequência é formada apenas pelo número zero.")

    #inicia contador, soma e define variáveis maior e menor
    else:
        cont = 0
        soma = 0
        maior = 0
        menor = 0

        #loop de N valores
        while N-1 >= cont:
            y = float(input("Digite um valor da sequência: "))

            #compara os valores
            if y > maior: maior = y
            elif menor == 0: menor = y
            elif y < menor: menor = y

            #soma os valores e adiciona ao contador
            soma = soma + y
            cont = cont + 1

        #imprime o resultado
        print ("O maior valor da sequência é:", maior, ", o menor valor é:", menor, "e a média dos valores é:", soma/N)
main()

