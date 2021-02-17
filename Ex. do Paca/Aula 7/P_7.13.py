#  Dados N > 0 verificar se N é palíndrome. Um número é palíndrome quando é o mesmo lido da direita
# para a esquerda ou da esquerda para a direita. Ou seja, o primeiro algarismo é igual ao último, o segundo igual
# ao penúltimo e assim por diante

def main ():

    n = int(input("Digite um número para verificar se ele é palíndrome: "))
    temp = n
    reverso = 0

    while n > 0:
        dig = n%10
        reverso = reverso*10 + dig
        n = n//10

    if temp == reverso:
        print ("O número", temp, "é palíndrome.")
    else: print ("O número", temp, "não é palíndrome.")

main ()


