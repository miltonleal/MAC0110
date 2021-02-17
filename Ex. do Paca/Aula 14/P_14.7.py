#Função Harmonico(sup) que recebe um valor sup > 0 e calcula a soma acima até que o valor da soma seja menor ou igual a sup.
# Note que o valor da soma é crescente e divergente.

def harmonico(sup):

    soma, k = 0, 1 # inicia a soma

    while soma <= sup:
        soma = soma + 1 / k
        k = k + 1
        if soma > sup:
            soma = soma - 1/k
            return soma

print(harmonico(2))
print(harmonico(3))
print(harmonico(4))
print(harmonico(5))
print(harmonico(6))
print(harmonico(7))
