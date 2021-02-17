# Dado n > 0 inteiro e uma sequência de n elementos, imprimir a sequência na ordem inversa a que foi lida.

def main ():


    seq = []
    n = int(input("Digite o valor de n: "))

    for i in range (n):
        seq.append((float(input("Digite o valor da sequência: "))))

    for j in range (-1, -(len(seq) +1), -1):
        print (seq[j], end = ' ')

main ()

