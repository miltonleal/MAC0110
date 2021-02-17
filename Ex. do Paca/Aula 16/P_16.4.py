# Dado n > 0 inteiro e uma sequência de n valores float, calcular a média e determinar o elemento da sequência que está mais próximo da média,
# ou seja, o elemento cuja diferença em módulo com a média seja mínima, considerando uma sequência de valores terminada por zero

def main ():

    seq = []
    cont = 0
    soma = 0

    while True:

        x = float(input("Digite o valor da sequência: "))

        seq.append(x)

        soma = soma + x

        cont = cont + 1

        if x == 0:
            break


    media = soma / (cont-1)
    print("a média é:", media)

    indmin, valmin = 0, abs(seq[0] - media)

    for i in range(1, cont):
        if valmin > abs(seq[i] - media):
            indmin, valmin = i, abs(seq[i] - media)

    print("o valor mais próxima da média: seq[", indmin, "]=", seq[indmin])

main ()

