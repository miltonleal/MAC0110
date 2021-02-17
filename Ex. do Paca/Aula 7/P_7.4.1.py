# Dado n ≥ 0, imprimir separadamente cada um dos dígitos de N na ordem inversa. Exemplo: se n é 1234, imprimir 4, 3, 2, 1.

def main ():

    #leia n
    n = int(input("Entre com o valor de n: "))

    while n > 0:
        digito = n % 10
        print (digito)
        n = n // 10
main ()
