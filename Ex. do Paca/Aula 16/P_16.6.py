# Dado n > 0 inteiro e uma sequência de n elementos, imprimir a sequência na ordem inversa a que foi lida.
# considerando uma sequência de valores terminada por zero

def main ():

    seq = []

    while True:

        x = float(input("Digite o valor da sequência: "))

        seq.append(x)

        if x == 0:
            break

    for j in range (-2, -(len(seq) +1), -1):
        print (seq[j], end = ' ')

main ()
