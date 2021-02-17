# P14.6) Função Harmonico(epsilon) que recebe número epsilon > 0 bem pequeno (exemplo: 0.00001) e calcula a soma de todos os termos maiores ou iguais a epsilon.
#Ou seja, calcular 1 + 1/2 + 1/3 + ... 1/k, tal que 1/i ≥ epsilon para i = 1, 2, ..., k e 1 / (k+1) < epsilon.


def harmonico(epsilon):

    h, k = 0, 1 # inicia a soma

    # Somar todos os termos maiores ou iguais a epsilon
    while 1 / k >= epsilon:
        h = h + 1 / k
        k = k + 1
    return h

print(harmonico(0.001))



