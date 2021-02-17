#Dados a e b inteiros maiores que 2, verificar quantos primos há no intervalo [a, b],
# ou seja os números maiores ou iguais a n e menores ou iguais a m.

def main():

    import math # vamos usar a função sqrt
    # definir o intervalo

    a = int(input("Entre com a:"))
    b = int(input("Entre com b:"))

    contap = 0

    # Variar k de 2 a n e testar cada k
    for k in range(a, b + 1):

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
            contap = contap + 1

    print("entre a e b existem", contap, "primos,")

while True:
    main()


