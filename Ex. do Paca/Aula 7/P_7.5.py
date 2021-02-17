# Dados os inteiros n > 0 e d (0 < d < 9), verificar quantas vezes o dígito d ocorre em n

def main ():

    #leia o número n e o número d
    n = int(input("Digite um número: "))
    d = int(input("Digite um número d tal que 0 ≤ d ≤ 9: "))
    cont = 0

    while n > 0:
        digito = n % 10
        if digito == d:
            cont = cont + 1
        n = n // 10
    print("O número de vezes que o dígito d apareceu no número inserido foi de:", cont)
main ()

