# Dado N > 0 e uma sequência de N números calcular a soma dos elementos da sequência:

def main ():

    #entrada de N
    N = int(input("Digite o número de elementos da sequência: "))

    #inicia a soma
    soma = 0

    #repete N vezes o programa
    for contador in range (N):
        x = int(input("Digite o valor: "))
        soma += x
    
    #imprime o resultado
    print ("valor total:", soma)

main ()
main ()
main ()
