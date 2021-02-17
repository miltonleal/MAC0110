# Dado n ≥ 0, imprimir separadamente cada um dos dígitos de N na ordem direta

def main ():

    #leia o número
    n = int(input("Digite um número: "))
    rev = 0
    dir = 0

    while n > 0:
        digito = n % 10
        rev = rev*10 + digito
        n = n // 10

    while rev > 0:
        dig = rev % 10
        dir = dir*10 + dig
        print (dig)
        rev = rev // 10
main()