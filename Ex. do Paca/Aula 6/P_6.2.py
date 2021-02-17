#Dado N > 0 e uma sequência de N números, determinar o menor elemento da sequência.

def main():
    #ler o número de elementos da sequência
    N = int(input("Digite a quantidade de números da sequência: "))

    #consistência dos dados de entrada de N
    if N == 0:
        print ("O número de elementos da sequência é zero.")
    else:
        menor = float(input("Digite o primeiro valor da sequência: "))

    #inicia o contador
        contador = 1

    #repete a operação
        while N -1 >= contador:
            x = float(input("Digite o próximo valor da sequência: "))
            #compara os valores
            if x < menor: menor = x
            contador = contador + 1
        #imprime o resultado
        print ("O menor valor da sequência é", menor)
main ()



