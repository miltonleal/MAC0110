#Escreva uma função Freq(numeros, a, b, k)que recebe uma lista numeros contendo
# valores float no intervalo [a, b), onde a < b. Ou seja, esses valores são todos maiores ou iguais a
# a e menores que b. Recebe também k > 0. O intervalo [a, b) deve ser dividido em k intervalos
# iguais de tamanho t = (b – a) / k. A função deve devolver uma lista com k contadores que
# contenham a quantidade de elementos em cada intervalo.

import math

j = [12.34, 22.12, 35.45, 0.1, 2, 9, 13]

def freq(numeros,a,b,k):

    f = k*[0]

    tam = (b-a)/k

    for i in range (len(numeros)):

        k = math.trunc(numeros[i] // tam)
        f[k] = f[k] +1

    return f

print(freq(j,0,100,10))




