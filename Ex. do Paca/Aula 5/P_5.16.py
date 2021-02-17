'''Dada uma sequência de números de ponto flutuante (positivos e/ou negativos)
terminada por zero, calcular a média dos positivos e a média dos negativos.'''

# inicia o x com valor diferente de zero
x = 1.5

# inicia o contador e a soma
contador = 0
soma = 0

# inicia a soma
while x != 0:
    x = float(input("Digite o próximo valor: "))
    if x != 0:
        contador = contador + 1
        soma = soma + x

# verifica se a sequência possui zero elementos e finaliza a soma e calcula a média
if contador == 0:
    print ("A sequência possui zero elementos")

else: print ("A média dos valores da sequência é:", soma/contador)
