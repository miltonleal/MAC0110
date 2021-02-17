# Dados 3 números imprimi-los em ordem crescente.
# Considere ordem crescente quando for menor ou igual ao seguinte.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b >= c:
    print(c, b, a)

elif a >= c >= b:
    print(b, c, a)

elif b >= a >= c:
    print(c, a, b)

elif b >= c >= a:
    print(a, c, b)

elif c >= a >= b:
    print(b, a, c)

elif c >= b >= a:
    print(a, b, c)
