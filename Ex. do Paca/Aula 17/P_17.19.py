#Escreva uma função Freq(numeros) que recebe uma lista numeros contendo valores entre 0 e 99 inteiros.
# Devolve uma lista f com 10 contadores onde f[0] = quantidade de valores entre 0 e 9,
# f[1] = quantidade de valores entre 10 e 19, ..., f[9] = quantidade de valores entre 90 e 99.


a = [1,12,34,45,67,65,64,78,98,67,34,32,32,12,23,34]

def freq_numeros(a):

    f = 10 * [0]

    for i in range(len(a)):

        k = a[i] // 10

        f[k] = f[k] + 1

    return f

print (freq_numeros(a))
