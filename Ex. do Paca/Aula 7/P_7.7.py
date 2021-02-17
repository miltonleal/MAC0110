# Dado um certo NUSP, verifique se e o seu NUSP é constituído por 7 dígitos: d1 d2 d3 d4 d5 d6 d7. Suponha que d7 é o dígito de
# redundância e que d7 deve ser igual a (d1*9 + d2*7 +d3*5 + d4*3 + d5*2 + d6*1) módulo 10.

def main ():

    NUSP = int(input("Digite o seu número USP: "))

    x = NUSP

    d1 = NUSP // 10**6

    d2 = NUSP % 10**6 // 10**5

    d3 = NUSP % 10**6 % 10**5 // 10**4

    d4 = NUSP % 10**6 % 10**5 % 10**4 // 10**3

    d5 = NUSP % 10**6 % 10**5 % 10**4 % 10**3 // 10**2

    d6 = NUSP % 10**6 % 10**5 % 10**4 % 10**3 % 10**2 // 10

    d7 = NUSP % 10**6 % 10**5 % 10**4 % 10**3 % 10**2 % 10

    d1d = d1*9
    d2d = d2*7
    d3d = d3*5
    d4d = d4*3
    d5d = d5*2
    d6d = d6*1

    y = (d1d+d2d+d3d+d4d+d5d+d6d) % 10

    if y != 0:
        d7d = 10 - y

        if d7d == d7:
            print ("O dígito verificador do NUSP inserido está de acordo com a regra.")
        else: print ("O dígito verificador do NUSP inserido não está de acordo com a regra.")

    else: print ("O dígito verificador do NUSP inserido não está de acordo com a regra.")



main ()
