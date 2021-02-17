# dado n inteiro, quantos elementos inteiros entre 0 e 999, determinar quantos entre 0 e 99, 100 e 199, ..., 900 e 999.

def main ():

    n = int(input("Digite o valor de n: "))

    f = 10 * [0]

    for i in range (n):
        x = int(input("digite o valor: "))
        k = x//100
        f[k] = f[k] + 1

    for j in range (10):
        print ("Existem", f[j], "elementos entre", j*100, "e", j*100 + 99)

main ()

