#Escreva uma função que compara duas datas que são dadas na forma dia, mês e ano.
# A função devolve um valor maior que zero se a primeira data é maior que a segunda, 0 se são iguais
# e um valor menor que zero se a segunda é maior que a primeira

def main ():

    dia_1 = int(input("Digite o dia da primeira data: "))
    mes_1 = int(input("Digite o mês da primeira data: "))
    ano_1 = int(input("Digite o ano da primeira data: "))
    dia_2 = int(input("Digite o dia da segunda data: "))
    mes_2 = int(input("Digite o mês da segunda data: "))
    ano_2 = int(input("Digite o ano da segunda data: "))

    print (ComparaData(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2))

def ComparaData(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2):

    while ano_1 != ano_2:

        if ano_2 > ano_1: return ano_1 - ano_2
        return ano_1 - ano_2

    while mes_1 != mes_2:

        if mes_2 > mes_1: return mes_1 - mes_2
        return mes_1 - mes_2

    while dia_1 != dia_2:

        if dia_2 > dia_1: return dia_1 - dia_2
        return dia_1 - dia_2

    if (dia_1, mes_1, ano_1) == (dia_2, mes_2, ano_2): return 0


main ()





