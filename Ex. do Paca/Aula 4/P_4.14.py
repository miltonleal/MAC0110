# Dados 3 números inteiros positivos verificar se são lados de
# algum triângulo, isto é, se o maior é menor que a soma dos outros dois.

a = int(input("Digite o tamanho do lado A do triângulo: "))
b = int(input("Digite o tamanho do lado B do triângulo: "))
c = int(input("Digite o tamanho do lado C do triângulo: "))

if a>=b and a>=c and a < b + c:
    print("Esses lados compõem um triângulo")

elif b>=a and a>=c and b < a + c:
        print("Esses lados compõem um triângulo")

elif c>=a and c>=b and c < a + b:
            print("Esses lados compõem um triângulo")

else:
    print("Esses lados não compõem um triângulo")

    
