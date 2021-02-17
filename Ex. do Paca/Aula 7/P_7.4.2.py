# Dado n ≥ 0, imprimir separadamente cada um dos dígitos de N na ordem direta

def main ():

    #leia o número e o expoente da potência de 10 próxima a ele
    n = int(input("Digite um número: "))
    m = (int(input("Digite o expoente da maior potência de 10 menor que n: ")))

    #realiza as divisões inteiras e com resto e redefine n e m
    while n > 0:
        digito = n // 10**m
        print (digito)
        n = n % (10**m)
        m = m -1
main ()


