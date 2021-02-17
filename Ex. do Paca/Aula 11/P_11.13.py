#Dado n, calcular todos os primos entre 2 e n.
#Lembre-se que n é primo se não tem divisores entre 2 e raiz de n.

def main ():
    # ler n inteiro >= 0
    n = int(input("Entre com o valor de n inteiro >= a dois: "))
    soma = 0

    # Variar k de 2 a n e testar cada k
    for k in range(2, n + 1):

        # verifica se k tem divisores entre 2 e a raiz de k
        div = 2  # primeiro candidato a divisor
        tem_div = False

        while div * div <= k:
            if k % div == 0:
                tem_div = True  # achou um divisor
                break  # sai do while
            div += 1  # testa o próximo candidato a divisor

            # verifica se encontrou algum divisor entre 2 a raiz de k
            # ou seja, se saiu do while pelo break ou não
        if not tem_div:
            soma = soma + k

    print("a soma é", soma)

while True:
    main()