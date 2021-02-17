#Função compara_listas(a, b) que compara o conteúdo das listas a e b. Devolve: len(a) se as listas são exatamente iguais.
# Ou seja, o comprimento das listas a e b. k se a[k] ≠ b[k] e a[i] = b[i] para 0 ≤ i < k.

a = [1,2,3,2,1,0,5]
b = [1,2,3,2,1,0,5,6]

def compara_listas(a,b):

        k = 0
        while k < min(len(a), len(b)):

            if a[k] == b[k]:
                pass
            else:
                return k
            k = k + 1

        return len(a)


print (compara_listas(a,b))



