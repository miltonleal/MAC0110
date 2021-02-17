#Dada uma sequência de números terminada por zero, determinar o maior elemento, o menor elemento e a média da sequência.

def main ():

    #lê o primeiro valor
    x = float(input("Digite o primeiro valor da sequência: "))

    #consistência dos dados
    if x == 0:
        print ("Esta sequência possui apenas o número zero como elemento.")

    # inicia soma, contador para fazer a média, define maior e menor
    else:
        soma = x
        maior = x
        menor = x
        cont = 0

        # inicia o loop para contabilização e comparação dos valores
        while x != 0:
            x = float(input("Digite o próximo valor da sequência: "))
            if x != 0 and x > maior: maior = x
            elif x != 0 and x < menor: menor = x
            soma = soma + x
            cont = cont + 1
        #imprime o resultado
        print ("O maior valor da sequência é", maior, ", o menor valor é", menor, "e a média é", soma/cont)
main()

