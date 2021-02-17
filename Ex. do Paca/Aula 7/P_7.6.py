# Dado um valor em reais V (com duas casas decimais, os centavos), determinar a quantidade máxima de
# notas de 100, 50, 20, 10, 5 2 e 1, moedas de 0,50, 0,25, 0,10, 0,05 e 0,01 necessárias para compor V.

def main ():

    V = float(input("Digite o total em R$ com até duas casas decimais: "))

    x = int(V * 100)

    n_100 = x // 10000

    n_50 = x % 10000 // 5000

    n_20 = x % 10000 % 5000 // 2000

    n_10 = x % 10000 % 5000 % 2000 // 1000

    n_5 = x % 10000 % 5000 % 2000 % 1000 // 500

    n_2 = x % 10000 % 5000 % 2000 % 1000 % 500 // 200

    n_1 = x % 10000 % 5000 % 2000 % 1000 % 500 % 200 // 100

    m_05 = x % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 // 50

    m_025 = x % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 // 25

    m_010 = x % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25 // 10

    m_005 = x % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25 % 10 // 5

    m_001 = x % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25 % 10 % 5 // 1

    print("O valor inserido pode ser composto por", n_100, "nota(s) de R$100,", n_50, "nota(s) de R$50,", n_20, "nota(s) de R$20,", n_10, "nota(s) de R$10,", n_5, "nota(s) de R$5,", n_2, "nota(s) de R$2,", n_1, "nota(s) de R$1 e", m_05, "moeda(s) de R$0,50,", m_025, "moeda(s) de R$0,25,", m_010, "moeda(s) de R$0,10,", m_005, "moeda(s) de R$0,05 e", m_001, "moeda(s) de R$0,01.")

main ()
