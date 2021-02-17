# Dado n > 0 inteiro e uma sequência de n valores float, calcular o maior, o menor e a média dos elementos da sequência.
# Em seguida verificar quais os elementos da sequência que são iguais à média.

def main ():


    # ler os elementos e inserir na lista
    seq = []
    n = int(input("Entre com n > 0 inteiro:"))

    for i in range(n):

        #x = float(input("entre com novo valor:"))
        #seq.append(x)

    # podia ser feito num só comando
        seq.append(float(input("entre com novo valor:")))

    # inicia maior, menor e media com o primeiro elemento
    maior, menor, media = seq[0], seq[0], seq[0]

    # varre seq a partir do segundo elemento
    for i in range(1, n):

        if maior < seq[i]: maior = seq[i]
        if menor > seq[i]: menor = seq[i]
        media = media + seq[i]
    # imprime resultado
    media = media / n
    print("Maior = ", maior, "Menor = ", menor, "Média = ", media)

    # procura agora aqueles iguais á média
    k = seq.count(media)
    if k == 0: print("Não há elemento igual a média")
    else:
        print("Há ", k, "elementos iguais á média - são eles:")

    ind_ini = 0
    for i in range(k):
        indx = seq.index(media, ind_ini)
        print("elemento ", indx)
    # inicia a nova busca no element seguinte
        ind_ini = indx + 1
main()