# P8.2) Dada uma sequência de números terminada por zero, calcular a soma dos elementos apenas dos números
# positivos. Ignorar os negativos.

def main():
    # inicia a soma
    soma = 0
    # loop infinito
    while True:
        # le o próximo dado
        x = int(input("Entre com o próximo: "))
        # se for negativo ignora esse dado e continua a repetição
        if x < 0: continue

        # se for zero abandona o loop
        # o comando abaixo é equivalente a if x == 0: break
        if not x: break

        soma = soma + x # adiciona

    # mostra a soma
    print("O valor da soma é:", soma)

main()