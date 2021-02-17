# Dado um certo CPF, verifique se segue a regra: O CPF possui 9 dígitos mais 2 de redundância.
# Supondo que os dois últimos dígitos sejam o resultado da seguinte fórmula: (d1*1 + d2*2 + ... + d9*9) módulo 100.

def main ():

    CPF = int(input("Digite o seu CPF: "))

    d1 = CPF // 10 ** 10

    d2 = CPF % 10 ** 10 // 10 ** 9

    d3 = CPF % 10 ** 10 % 10 ** 9 // 10 ** 8

    d4 = CPF % 10 ** 10 % 10 ** 9 % 10 ** 8 // 10 ** 7

    d5 = CPF % 10 ** 10 % 10 ** 9 % 10 ** 8 % 10 ** 7 // 10 ** 6

    d6 = CPF % 10 ** 10 % 10 ** 9 % 10 ** 8 % 10 ** 7 % 10 ** 6 // 10 ** 5

    d7 = CPF % 10 ** 10 % 10 ** 9 % 10 ** 8 % 10 ** 7 % 10 ** 6 % 10 ** 5 // 10 ** 4

    d8 = CPF % 10 ** 10 % 10 ** 9 % 10 ** 8 % 10 ** 7 % 10 ** 6 % 10 ** 5 % 10 ** 4 // 10 ** 3

    d9 = CPF % 10 ** 10 % 10 ** 9 % 10 ** 8 % 10 ** 7 % 10 ** 6 % 10 ** 5 % 10 ** 4 % 10 ** 3 // 10 ** 2

    d10_11 = CPF % 10 ** 10 % 10 ** 9 % 10 ** 8 % 10 ** 7 % 10 ** 6 % 10 ** 5 % 10 ** 4 % 10 ** 3 % 10 ** 2 % 100

    formula = (d1*1) + (d2*2) + (d3*3) + (d4*4) + (d5*5) + (d6*6) + (d7*7) + (d8*8) + (d9*9)

    modulo100 = formula % 100

    if modulo100 != 0:
        y = 100 - modulo100
        if y == d10_11:
            print ("CPF confere")
        else: print ("CPF não confere")







main ()

