#Dada uma sequência de números terminada por zero, determinar o maior elemento da sequência.

def main():
    #lê o primeiro elemento
    x = float(input("Digite o primeiro elemento da sequência: "))

    #consistência dos dados
    if x == 0:
        print("Esta sequência possui apenas o número zero como elemento.")

    #determina que o x até então é o maior
    else:
        maior = x

    #inicia o loop
        while x != 0:
            x = float(input("Digite o próximo elemento da sequência: "))
            if x != 0 and x > maior: maior = x
        #saiu do loop
        print("O maior elemento da sequência é:", maior)
main()
