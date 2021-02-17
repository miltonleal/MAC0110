# Exercício-Programa 1 - Dispensador de Notas - MAC 110 - 1º semestre 2020
# Instituto de Matemática e Estatística da Universidade de São Paulo (IME/USP)
# Bacharelado em Matemática Aplicada Computacional (BMAC)
# Aluno: Milton Leal Neto - Número USP: 8973974

def main():

    print ("* * * Dispensador de Notas * * *") #nome do programa

    valor = 1

    while valor > 0:

        while True: #loop para realização da consistência dos dados inseridos pelo usuário
            try:
                v = int(input("\nValor do saque: ")) #requisita o valor a ser inserido pelo usuário

            except:
                print ("\n* * * Erro - valor digitado inválido") #caso usuário digite caractere diferente de um int > 0

            else:
                if v <= 0: #termina o programa caso o usuário digite um valor <= 0
                    print("\n* * * Fim do programa * * *")
                    quit()

                elif v % 10 != 0: #caso o usuário digite um int > 0 que não seja múltiplo de 10
                    print("\n* * * Erro - Valor do saque deve ser múltiplo de R$10")

                    continue #retoma o loop para o usuário reinserir o valor em caso de erro

                break #sai do loop

        v_aux = v #variável auxiliar para o valor inserido pelo usuário

        opt = 4 #número máximo de opções de combinações das notas

        if v_aux >= 100: #valor maior que 100

            print("\nOpção %d : Notas Quantidade" % (opt - 3)) #Opção 1
            print("%14d %6d" % (100, v_aux // 100)) #imprime total de notas
            if v_aux % 100 // 50 != 0: print("%14d %6d" % (50, v_aux % 100 // 50)) #imprime total de notas se != 0
            if v_aux % 100 % 50 // 20 != 0: print("%14d %6d" % (20, v_aux % 100 % 50 // 20))
            if v_aux % 100 % 50 % 20 // 10 != 0: print("%14d %6d" % (10, v_aux % 100 % 50 % 20 // 10))

            print("\nOpção %d : Notas Quantidade" % (opt - 2)) #Opção 2
            if v_aux // 50 != 0: print("%14d %6d" % (50, v_aux // 50))
            if v_aux % 50 // 20 != 0: print("%14d %6d" % (20, v_aux % 50 // 20))
            if v_aux % 50 % 20 // 10 != 0: print("%14d %6d" % (10, v_aux % 50 % 20 // 10))

            print("\nOpção %d : Notas Quantidade" % (opt - 1)) #Opção 3
            if v_aux // 20 != 0: print("%14d %6d" % (20, v_aux // 20))
            if v_aux % 20 // 10 != 0: print("%14d %6d" % (10, v_aux % 20 // 10))

            print("\nOpção %d : Notas Quantidade" % (opt)) #Opção 4
            if v_aux // 10 != 0: print("%14d %6d" % (10, v_aux // 10))

        elif v_aux >= 50 and v_aux <= 90: #valor entre 50 e 90

            print("\nOpção %d : Notas Quantidade" % (opt - 3)) #Opção 1
            print("%14d %6d" % (50, v_aux // 50))
            if v_aux % 50 // 20 != 0: print("%14d %6d" % (20, v_aux % 50 // 20))
            if v_aux % 50 % 20 // 10 != 0: print("%14d %6d" % (10, v_aux % 50 % 20 // 10))

            print("\nOpção %d : Notas Quantidade" % (opt - 2)) #Opção 2
            print("%14d %6d" % (20, v_aux // 20))
            if v_aux % 20 // 10 != 0: print("%14d %6d" % (10, v_aux % 20 // 10))

            print("\nOpção %d : Notas Quantidade" % (opt - 1)) #Opção 3
            print("%14d %6d" % (10, v_aux // 10))

        elif v_aux >= 20 and v_aux <= 40: #valor entre 20 e 40

            print("\nOpção %d : Notas Quantidade" % (opt - 3)) #Opção 1
            print("%14d %6d" % (20, v_aux // 20))
            if v_aux % 20 // 10 != 0: print("%14d %6d" % (10, v_aux % 20 // 10))

            print("\nOpção %d : Notas Quantidade" % (opt - 2)) #Opção 2
            print("%14d %6d" % (10, v_aux // 10))

        else:
            v_aux == 10 #valor igual a 10
            print("\nOpção %d : Notas Quantidade" % (opt - 3)) #Opção 1
            print("%14d %6d" % (10, 1))

main()
