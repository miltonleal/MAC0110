#   Dado N > 0 e uma sequência de números diferentes de zero, calcular a média dos positivos e a média
# dos negativos

# entrada de N
N = int(input("Quantos números você gostaria de calcular a média? "))

# inicia o contador e a soma
contador = 0
soma = 0

# consistência dos dados

while N == 0:
    N = float(input("Digite um valor maior que zero: "))

# repete N vezes o trecho do programa que faz a soma
while contador < N:
    x = float(input("Digite um número para ser somado: "))
    soma = soma + x
    contador = contador + 1

# imprime a média da soma

print("A média da soma dos números é", soma/N)

