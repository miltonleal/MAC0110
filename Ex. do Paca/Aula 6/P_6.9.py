'''Dado um valor float em reais (R$), entre R$0,01 e R$0,99, determinar quantas moedas de R$0,50, R$0,25, R$10,
R$0,05 e R$0,01 são necessárias para compor esse valor. A solução procurada é aquela com o máximo de moedas de
cada tipo. Sugestão: Multiplicar o valor dado por 100 e transformá-lo em inteiro com a função int.'''

N = float(input("Digite um valor entre R$0.01 e R$0.99: "))

N_inteiro = int(N*100)

Total_50 = N_inteiro // 50

Total_25 = N_inteiro % 50 // 25

Total_10 = N_inteiro % 50 % 25 // 10

Total_5 = N_inteiro % 50 % 25 % 10 // 5

Total_1 = N_inteiro % 50 % 25 % 10 % 5 // 1

print("Você precisará de", Total_50, "moedas de R$0,50", Total_25, "moedas de R$0,25", Total_10, "moedas de R$0,10", Total_5, "moedas de R$0,05 e", Total_1, "moedas de R$0,01.")
