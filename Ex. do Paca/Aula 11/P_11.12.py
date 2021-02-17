# Dados a e b, dizer quais números são primos e quais não são no intervalo [a, b),
# ou seja, maiores ou iguais a a e menores que b.

def main():

    import math # vamos usar a função sqrt
    # definir o intervalo

    a = int(input("Entre com a:"))
    b = int(input("Entre com b:"))

    for num in range(a, b): # variar num no intervalo [a, b)
    # testar todos os divisores de 2 até a raiz de num
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0: # se ocorrer, i e’ fator
                j = num / i # calcule o outro fator
                print ('%d igual a %d * %d' % (num,i,j))
                break # passe a verificar o próximo número

        else: # else do for - executa se esgotar o for
            print (num, "e' numero primo")
main()