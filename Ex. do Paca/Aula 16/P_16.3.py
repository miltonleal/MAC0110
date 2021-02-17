# Dado n > 0 inteiro e uma sequência de n valores float, calcular a média e determinar o elemento da sequência que está mais próximo da média,
# ou seja, o elemento cuja diferença em módulo com a média seja mínima.

def main ():

    seq = []
    n = int(input("Digite o valor de n: "))

    for i in range (n):
        seq.append((float(input("Digite o valor da sequência: "))))

    media = seq[0]

    for i in range (1,n):
        media = media + seq[i]

    media = media/n
    print ("a média é:", media)

    indmin, valmin = 0, abs(seq[0] - media)

    for i in range (1,n):
        if valmin > abs(seq[i] - media):
            indmin, valmin = i, abs(seq[i] - media)

    print ("o valor mais próxima da média: seq[", indmin, "]=", seq[indmin])




main ()

