#Considere a sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8, ... Começa com 0 e 1 e cada elemento
#seguinte é a soma dos dois anteriores. Escreva uma função que recebe n ≥ 0 e imprime todos os
#números da sequência menores ou iguais a n.

def fibonacci(n):

    """Imprime a sequência de Fibonacci dos menores que n."""
    a, b = 0, 1 # 0 e 1 são os 2 primeiros

    # imprime todos os menores ou iguais a n
    while a <= n:
        print(a)
        # a e b são os 2 seguintes
        a, b = b, a + b

# exemplo de chamada
print (fibonacci(8))

