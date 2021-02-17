# Dado n > 0 inteiro e uma sequência de n valores float, calcular o maior, o menor e a média dos elementos da sequência.
# Em seguida verificar quais os elementos da sequência que são iguais à média.
# No trecho final, não usar as funções count e index. Isto é, escreva um trecho que percorra a lista,
# verificando se cada elemento é igual à média e também conte quantos elementos iguais à média existem

def main ():

    seq = []
    n = int(input("Digite o valor de n: "))

    for i in range (n):
        seq.append((float(input("Digite o valor da sequência: "))))


    maior, menor, media = seq[0], seq[0], seq[0]

    for i in range (1,n):

        if maior < seq[i]: maior = seq[i]
        if menor > seq[i]: menor = seq[i]
        media = media + seq[i]

    media = media/n
    print("Maior =", maior, "Menor =", menor, "Media =", media)

    indice = []
    cont = 0
    for k in range (len(seq) -1):
        if k == media: cont += 1
        if k == media: indice.append(k-1)

    if cont == 0: print ("Não existem elementos iguais à média.")
    else:
        print ("Existem", cont, "elementos iguais à média.")

    print("O elemento igual está localizado no índice", indice)



main()

