
'''
Dados a e b float (a < b), n e k inteiros e maiores que 0, uma sequência de n valores float no intervalor [a, b),
ou seja maiores ou iguais a a e menores que b. Dividir o intervalo [a, b) em k subintervalos iguais e determinar quantos
estão em cada intervalo. Note que serão k contadores e o tamanho do intervalor é t = (b – a) / k:
f[0] = elementos ≥ a e < a + t * 1
f[1] = elementos ≥ a + t * 1 e < a + t * 2
...
f[k-1] = elementos ≥ a + t * (k-1) e < a + t * k = b

'''

import math

def main ():

    a = float(input("digite o valor de a: "))
    b = float(input("digite o valor de b: "))
    n = int(input("digite o valor de n: "))
    k = int(input("digite o valor de subintervalos: "))

    f = k * [0]

    t = (b - a) / k

    for i in range (n):
        x = float(input("digite o valor da sequência: "))
        ind = math.trunc((x-a)//t)
        f[ind] = f[ind] + 1

    for i in range (k):
        print("Há ", f[i], "elementos >=", a+(t*i), "e <", a+(t*(i+1)))

main()





