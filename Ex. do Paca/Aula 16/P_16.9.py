# n inteiros entre 0 e 999, determinar quantos entre 0 e 9, 10 e 19, ..., 990 e 999

def main ():

    n = int(input("Digite o valor de n: "))

    f = 100 * [0]

    for i in range (n):
        x = int(input("digite o valor: "))
        k = x//10
        f[k] = f[k] + 1

    for j in range (100):
        print ("Existem", f[j], "elementos entre", j*10, "e", j*10 + 9)

main ()
