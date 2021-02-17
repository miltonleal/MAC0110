# Dado um número inteiro n ≥ 0, calcular o fatorial de n (n!). Outra maneira

def main():

    n = int(input("Digite o valor de n: "))

    # inicia as variáveis
    fat, i = 1, 2

    while i <= n:
        fat *= i
        i += 1

    # resultado
    print("O valor de %d! eh =" %n, fat)

#--------------------------------------------

main()