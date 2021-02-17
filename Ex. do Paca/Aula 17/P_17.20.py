#Idem se os valores estão entre 0 e 999. Neste caso a lista devolvida terá 100 valores:
# f[0] = quantidade de valores entre 0 e 9, f[1] = quantidade de valores entre 10 e 19, ..., f[99] = entre 990 e 999.


a = [1,12,34,45,67,65,64,78,98,67,34,32,32,12,23,34,200,500,300,789,990,340]

def freq_numeros(a):

    f = 100 * [0]

    for i in range(len(a)):

        k = a[i] // 10

        f[k] = f[k] + 1

    return f

print (freq_numeros(a))
