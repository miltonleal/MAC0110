'''Dado um valor inteiro em reais (R$), determinar quantas notas de R$100, R$50, R$20, R$10, R$5, R$2 e R$1
são necessárias para compor esse valor. A solução procurada é aquela com o máximo de notas de cada tipo.'''

N = int(input("Digite o valor total em R$: "))

total_100 = N // 100

total_50 = N % 100 // 50

total_20 = N % 100 % 50 // 20

total_10 = N % 100 % 50 % 20 // 10

total_5 = N % 100 % 50 % 20 % 10 // 5

total_2 = 100 % 50 % 20 % 10 % 5 // 2

total_1 = 100 % 50 % 20 % 10 % 5 % 2 // 1

print ("Serão necessárias", total_100, "nota(s) de R$100", total_50, "nota(s) de R$50", total_20, "nota(s) de R$20", total_10, "nota(s) de R$10", total_5, "nota(s) de R$5", total_2, "nota(s) de R$2 e",  total_1, "nota(s) de R$1")