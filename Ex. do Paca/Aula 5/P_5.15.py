''' Dada uma sequência de números inteiros (positivos e/ou negativos)
terminada por zero, calcular a média dos positivos e a média dos negativos. '''

# inicia x com um valor diferente de zero
x = 1

# inicia o contador e a soma
contador = 0
soma = 0

# lê o próximo elemento e soma
while x != 0:
    x = int(input("Digite o valor da sequência: "))
    if x != 0:
        contador = contador + 1
        soma = soma + x

if contador == 0:
    print ("A sequência possui zero elementos")

else: print("A média da soma dos elementos é:", soma/contador)


