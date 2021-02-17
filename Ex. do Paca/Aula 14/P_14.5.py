#Função Harmonico(n) que recebe inteiro n > 0 e devolve o valor da soma: 1 + 1/2 + 1/3 + 1/4 + . . . + 1/n.
# Esta soma é conhecida como o n-ésimo número harmônico.


def harmonico (n):

    soma = 0

    for i in range (1, n + 1):

        soma = soma + 1/i

    print(soma)

harmonico (10)