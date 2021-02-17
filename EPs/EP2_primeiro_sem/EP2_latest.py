# Exercício-Programa 2 - Cálculo de funções por séries de Taylor - MAC 110 - 1º semestre 2020
# Instituto de Matemática e Estatística da Universidade de São Paulo (IME/USP)
# Bacharelado em Matemática Aplicada Computacional (BMAC)
# Aluno: Milton Leal Neto - Número USP: 8973974

########################################### DICIONÁRIO DE VARIÁVEIS ##############################################

# x = valor inserido pelo usuário para cálculo das funções seno, cosseno e exponencial
# n = valor inserido pelo usuário que estabelece o número de termos da soma da série de Taylor
# eps = valor inserido pelo usuário que estabelece que a soma seja executada até que um termo dela seja < que eps

# x_reduzido = reduz o valor de x para a 1ª volta do ciclo trigonométrico
# num = variável auxiliar para o x_reduzido
# sinal = sinal da expressão
# k = contador que serve como referência para o número de termos e também para o cálculo do fatorial
# fat = fatorial
# soma = valor da somatória da série de Taylor
# termo = expressão que generaliza o termo da soma

###################################################################################################################

import math

print("\n*** CÁLCULO DE FUNÇÕES POR SÉRIES DE TAYLOR ***")  # título do programa

### FUNÇÃO PRINCIPAL
def taylor_series():

    ### REQUISIÇÃO DOS DADOS DE ENTRADA
    while True:  # requisita o valor de x
        try:
            x = float(input("\nInsira o valor de x no intervalo [-100,100]: "))
            if x >= -100 and x <= 100:  # estabelece a limitação do intervalo de x
                break
            else:
                print("\nO valor de x deve estar no intervalo [-100,100]")
                continue
        except:  # avisa sobre um erro no entrada do valor
            print("\n* * * Erro - valor digitado inválido")

    while True:  # requisita o valor de n
        try:
            n = int(input("\nInsira o valor de n: "))
            break
        except:
            print("\n* * * Erro - valor digitado inválido")

    while True:  # requisita o valor de eps
        try:
            eps = float(input("\nInsira o valor de eps no intervalo ]0,1[: "))
            if eps > 0 and eps < 1:  # estabelece a limitação do intervalo de eps
                break
            else:
                print("\nO valor de eps deve estar dentro do intervalo ]0, 1[")
                continue
        except:
            print("\n* * * Erro - valor digitado inválido")

    ### LOOP PRINCIPAL
    while True:

        ### SENO - MÉTODO 1
        def seno_termos(x, n):  # função calcula seno com base em n termos da soma de Taylor

            x_reduzido = x % (2 * math.pi)
            num, sinal, k, fat, soma = x_reduzido, 1, 1, 1, 0

            while k <= n:  # loop que realiza a soma da série
                try:
                    soma += num * sinal / fat  # adiciona à soma o termo +- x^(2k+1)/(2k+1)!
                    num *= x_reduzido * x_reduzido  # eleva o x às potências ímpares
                    sinal *= -1  # alterna o sinal do x
                    fat *= (2 * k) * (2 * k + 1)  # calcula o fatorial dos números ímpares
                    k += 1  # adiciona uma unidade ao contador
                except OverflowError:
                    break  # evita erro por overflow
            return soma  # devolve a soma, ou seja, o valor do seno

        ### SENO - MÉTODO 2
        def seno_eps(x, eps):  # função calcula seno até que um termo da soma seja < que a precisão inserida

            x_reduzido = x % (2 * math.pi)
            num, sinal, k, fat, soma = x_reduzido, 1, 1, 1, 0

            while True:  # loop que realiza a soma da série
                try:
                    soma += num * sinal / fat  # adiciona à soma o termo +- x^(2k+1)/(2k+1)!
                    num *= x_reduzido * x_reduzido  # eleva o x às potências ímpares
                    sinal *= -1  # alterna o sinal do x
                    fat *= (2 * k) * (2 * k + 1)  # calcula o fatorial dos números ímpares
                    k += 1  # adiciona uma unidade ao contador
                    if abs(num * sinal / fat) < eps:  # compara o último termo com o valor do eps
                        return soma  # devolve a soma, ou seja, o valor do seno
                except OverflowError:
                    break  # evita erro por overflow

        ### COSSENO - MÉTODO 1
        def cos_termos(x, n):  # função calcula cosseno com base em n termos da soma de Taylor

            x_reduzido = x % (2 * math.pi)
            num, sinal, k, fat, soma = x_reduzido * x_reduzido, -1, 2, 2, 1

            while k <= n:
                try:
                    soma += num * sinal / fat  # adiciona à soma o termo +- x^2k/(2k)!
                    num *= x_reduzido * x_reduzido  # eleva o x às potências pares
                    sinal *= -1  # alterna o sinal do x
                    fat *= (2 * k - 1) * (2 * k)  # calcula o fatorial dos números pares
                    k += 1  # adiciona uma unidade ao contador
                except OverflowError:
                    break  # evita erro por overflow
            return soma  # devolve a soma, ou seja, o valor do cosseno

        ### COSSENO - MÉTODO 2
        def cos_eps(x, eps):  # função calcula cosseno até que um termo da soma seja < que a precisão inserida

            x_reduzido = x % (2 * math.pi)
            num, sinal, k, fat, soma = x_reduzido * x_reduzido, -1, 2, 2, 1

            while True:
                try:
                    soma += num * sinal / fat  # adiciona à soma o termo +- x^2k/(2k)!
                    num *= x_reduzido * x_reduzido  # eleva o x às potências pares
                    sinal *= -1  # alterna o sinal do x
                    fat *= (2 * k - 1) * (2 * k)  # calcula o fatorial dos números pares
                    k += 1  # adiciona uma unidade ao contador
                    if abs(num * sinal / fat) < eps:  # compara o último termo com o valor do eps
                        return soma  # devolve a soma, ou seja, o valor do cosseno
                except OverflowError:
                    break  # evita erro por overflow

        ### EXPONENCIAL - MÉTODO 1
        def exp_termos(x, n):  # função calcula exponencial com base em n termos da soma de Taylor

            soma, fat, k, num = 1, 1, 1, abs(x)
            lista = []  # lista para guardar os valores da soma

            while k <= n:
                try:
                    soma += num / fat  # adiciona à soma o termo + x^n/n!
                    num *= abs(x)  # eleva o x à próxima potência e recebe o módulo de x
                    k += 1  # adiciona uma unidade ao contador
                    fat *= k  # calcula o fatorial
                    lista.append(soma)  # adiciona o último valor da soma à lista
                except OverflowError:  # evita erro por overflow
                    break

            for j in lista:  # varre a lista para saber qual o último número diferente de "inf" ou "nan"
                if "inf" not in str(j) and "nan" not in str(j):
                    soma = j  # variável soma recebe o último número calculado

            if x < 0:  # caso x negativo, ajusta o resultado da função
                return 1 / soma  # devolve a soma, ou seja, o valor da exponencial
            else:
                return soma  # devolve a soma, ou seja, o valor da exponencial

        ### EXPONENCIAL - MÉTODO 2
        def exp_eps(x, eps):  # função calcula exponencial até que um termo da soma seja < que a precisão inserida

            soma, fat, k, num = 1, 1, 1, abs(x)
            lista = []  # lista para guardar os valores da soma

            while True:
                try:
                    soma += num / fat  # adiciona à soma o termo + x^n/n!
                    num *= abs(x)  # eleva o x à próxima potência e recebe o módulo de x
                    k += 1  # adiciona uma unidade ao contador
                    fat *= k  # calcula o fatorial
                    lista.append(soma)  # adiciona o último valor da soma à lista
                    if abs(num / fat) < eps:  # compara o último termo com o valor do eps
                        break
                except OverflowError:  # evita erro por overflow
                    break

            for j in lista:  # varre a lista para saber qual o último número diferente de "inf" ou "nan"
                if "inf" not in str(j) and "nan" not in str(j):
                    soma = j  # variável soma recebe o último número calculado

            if x < 0:  # caso x negativo, ajusta o resultado da função
                return 1 / soma  # devolve a soma, ou seja, o valor da exponencial
            else:
                return soma  # devolve a soma, ou seja, o valor da exponencial

        ### RESULTADO
        print("\nValores calculados para:")
        print("x =", x)
        print("n =", n)
        print("eps =", eps)

        print("\nSeno:")
        print("%24s%20s%s" % ("Usando a função math.sin", "- Valor Calculado: ", math.sin(x)))
        print("%24s%20s%s%32s%s" % ("Método 1 – qte de termos", "– Valor Calculado: ", seno_termos(x, n), " - |Diferença|: ",abs(math.sin(x) - seno_termos(x, n))))
        print("%18s%26s%s%32s%s" % ("Método 2 – epsilon", "– Valor Calculado: ", seno_eps(x, eps), " - |Diferença|: ",
                                    abs(math.sin(x) - seno_eps(x, eps))))

        print("\nCosseno:")
        print("%24s%20s%s" % ("Usando a função math.cos", "- Valor Calculado: ", math.cos(x)))
        print("%24s%20s%s%32s%s" % (
        "Método 1 – qte de termos", "– Valor Calculado: ", cos_termos(x, n), " - |Diferença|: ",
        abs(math.cos(x) - cos_termos(x, n))))
        print("%18s%26s%s%32s%s" % ("Método 2 – epsilon", "– Valor Calculado: ", cos_eps(x, eps), " - |Diferença|: ",
                                    abs(math.cos(x) - cos_eps(x, eps))))

        print("\nExponecial:")
        print("%24s%20s%s" % ("Usando a função math.exp", "- Valor Calculado: ", math.exp(x)))
        print("%24s%20s%s%32s%s" % (
        "Método 1 – qte de termos", "– Valor Calculado: ", exp_termos(x, n), " - |Diferença|: ",
        abs(math.exp(x) - exp_termos(x, n))))
        print("%18s%26s%s%32s%s" % ("Método 2 – epsilon", "– Valor Calculado: ", exp_eps(x, eps), " - |Diferença|: ",
                                    abs(math.exp(x) - exp_eps(x, eps))))

        print("\n* * * * * * * * *")

        #LOOP PARA NOVO CÁLCULO
        while True:
            try:
                novo_calc = input("\nNovo cálculo (S/N): ")
            except:
                pass
            else:
                if novo_calc == "n" or novo_calc == "N":  # caso usuário não queria mais continuar
                    print("\n*** Fim do programa ***")
                    quit()

                elif novo_calc == "s" or novo_calc == "S":  # caso o usuário queira realizar novo cálculo
                    break

                elif novo_calc != "n" or "N" or "S" or "s":  # tratamento de exceção
                    print("\nPor favor, digite uma entrada válida")
                    continue
                break

        ### REQUISIÇÃO DOS NOVOS DADOS DE ENTRADA
        while True:
            try:
                x_ = input("\nInsira o valor de x ou aperte enter para utilizar o valor anterior: ")
                if x_ == "":
                    x_ = x  # caso o usuário digite apenas enter, o sistema reutiliza o valor inserido

                elif float(x_) < -100 or float(
                        x_) > 100:  # trata exceção, caso x não esteja dentro do intervalo esperado
                    print("\nO valor de x deve estar no intervalo [-100,100]")
                    continue

                x = float(x_)  # transforma o dado de entrada em float
                break

            except:
                print("\n* * * Erro - valor digitado inválido")  # tratamento de exceção
                continue

        while True:
            try:
                n_ = input("\nInsira o valor de n ou aperte enter para utilizar o valor anterior: ")
                if n_ == "": n_ = n  # caso o usuário digite apenas enter, o sistema reutiliza o valor inserido

                n = int(n_)  # transforma o dado de entrada em inteiro
                break

            except:
                print("\n* * * Erro - valor digitado inválido")  # tratamento de exceção
                continue

        while True:
            try:
                eps_ = input("\nInsira o valor de eps ou aperte enter para utilizar o valor anterior: ")
                if eps_ == "":
                    eps_ = eps  # caso o usuário digite apenas enter, o sistema reutiliza o valor inserido

                elif float(eps_) <= 0 or float(
                        eps_) >= 1:  # trata exceção, caso eps não esteja dentro do intervalo esperado
                    print("\nO valor de eps deve estar no intervalo ]0,1[")
                    continue

                eps = float(eps_)  # transforma o dado de entrada em float
                break

            except:
                print("\n* * * Erro - valor digitado inválido")  # tratamento de exceção
                continue

taylor_series()















