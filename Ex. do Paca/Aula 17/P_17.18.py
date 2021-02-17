#Função Fibonacci(n) que devolve uma lista com a sequência de Fibonacci dos menores que n.

def fibo(n):

    result =[]
    a,b = 0,1

    while a < n:
        result.append(a)
        a,b = b, a+b
    return result

print (fibo(100))