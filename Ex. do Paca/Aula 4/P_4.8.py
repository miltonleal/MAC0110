#  Dados 2 números imprimi-los em ordem crescente.
# Considere ordem crescente quando o primeiro é menor ou igual ao segundo.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a>b: print(b,a)
elif b>a: print(a,b)
else: print("Os números são iguais")
