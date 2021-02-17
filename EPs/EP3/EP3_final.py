# Exercício-Programa 3 - Palpites meio aleatórios da Mega-Sena - MAC 110 - 1º semestre 2020
# Instituto de Matemática e Estatística da Universidade de São Paulo (IME/USP)
# Bacharelado em Matemática Aplicada Computacional (BMAC)
# Aluno: Milton Leal Neto - Número USP: 8973974

import random

print("\n*** PALPITES MEIO ALEATÓRIOS DA MEGA-SENA ***\n")

print("FASE 1:\nLeitura do arquivo de sorteios\nMontagem da tabela do último sorteio de cada número\n")

def leia_matriz():

    lista_aniversario = [] #cria uma lista vazia que receberá os dados das linhas do arquivo txt

    while True:
        try:
            arq = open(input("Entre com o nome do arquivo: "), "r") #abre o arquivo
            lines = arq.readlines() #retorna uma lista que contém cada linha do arquivo como um item da lista
        except:
            print("\nErro na abertura do arquivo. Insira novamente o nome do arquivo.\n")
            continue

        for linha in reversed(lines): #lê cada elemento da lista lines de trás para frente

            try:
                lin = linha[:len(linha)-1] #variável que recebe cada linha do arquivo de texto original como uma string
                v = lin.split('\t') #variável que recebe a linha acima e a transforma em uma lista com 8 elementos

                for j in range(8):

                    if j == 0 or j == 1: #se j = número do sorteio ou data
                        lista_aniversario.append(v[j]) #adiciona na lista de aniversário como string

                    else: #se j = número sorteado
                        if int(v[j]) not in lista_aniversario: #verifica se o número consta na tabela de aniversário
                            lista_aniversario.append(int(v[j])) #adiciona à lista de aniversário como inteiro caso não esteja na lista

                if len(lista_aniversario)> 180: #condição para quando a lista atingir o limite máximo de elementos da tabela [60 x (nº de sorteio, data e nº sorteado)]

                    while True: #loop para eliminar possíveis dados desnecessários da tabela
                        if type(lista_aniversario[len(lista_aniversario) -1]) == str:
                            del lista_aniversario[len(lista_aniversario) -1]
                        else:
                            break #sai do loop while
            except:
                pass

        arq.close()
        return lista_aniversario

lista_aniversario = leia_matriz()

### cria lista apenas com os números sorteados

lista_numeros = []

for i in range(len(lista_aniversario)): #varre a lista de aniversário
    if type(lista_aniversario[i]) == int: #se for int, ou seja, se for número sorteado
        lista_numeros.append(lista_aniversario[i]) #adiciona à lista que abriga somente os 60 números da Mega-Sena

lista_numeros.reverse() #coloca a lista com os números sorteados em ordem do mais antigo sorteado para o mais novo

### cria a matriz que será a tabela impressa na saída

matriz_aniversario = [3*[0] for i in range (60)] #matriz que recebe os dados da lista_aniversario

k = 0 #contador

while k <= 60: #tamanho total de linhas da matriz_aniversario

    matriz_aniversario[k][0] = lista_aniversario[0] #adiciona o número do sorteio à matriz
    matriz_aniversario[k][1] = lista_aniversario[1] #adiciona a data do sorteio
    matriz_aniversario[k][2] = lista_aniversario[2] #adiciona o número sorteado naquele sorteio
    try:
        if type(lista_aniversario[3]) == int: #verifica se o quarto elemento da lista de aniversário é um número sorteado
            del lista_aniversario[2] #se sim, deleta o número sorteado anterior
            k = k + 1 #acrescenta o contador para incluir o próximo número sorteado dentro do sorteio correto

        #verifica se o quarto, quinto e sexto elemento são strings, ou seja, se são o número do sorteio ou a data.
        elif type(lista_aniversario[3]) == str and type(lista_aniversario[4]) == str and type(lista_aniversario[5]) == str:
            del lista_aniversario[3], lista_aniversario[3] #deleta sorteios que não tenham números que interessam à matriz

        else:
            #caso tenha terminado de agregar os dados de um sorteio, deleta as informações daquele sorteio para seguir para o próximo
            del lista_aniversario[0],lista_aniversario[0],lista_aniversario[0]
            k = k + 1
    except:
        break

matriz_aniversario.reverse() #reordena a matriz do mais antigo para o mais novo sorteio

### Impressão da matriz que traz os números sorteados, sorteio e data

print("\nNúmeros sorteados há mais tempo na Mega-Sena:")

print("\nNúmero     Sorteio      Data")
for i in matriz_aniversario: #imprime a matriz_aniversario

    print("%4s%12s%15s" %(i[2], i[0], i[1]))

### SEGUNDA FASE DO PROGRAMA

print("\nFASE 2\nEscolha da aposta:")

while True: #loop principal

    while True:
        try:
            np = int(input("\nQuantidade de números da aposta: ")) #recebe a quantidade de números a serem apostados
            if np <6 or np > 12: #consistência dos valores
                print("\nA quantidade de números da aposta deve estar entre [6,12], considerando apenas números inteiros.")
                continue
        except:
            print("\n*** Erro *** Entrada inválida ***")
            continue
        else:
            break

    while True:
        try:
            nt = int(input("\nEscolher dentre quantos menos recentes: ")) #recebe a quantidade de números a serem levados em consideração para a aposta
            if nt < np or np > 60: #consistência dos valores
                print("\nA quantidade de números recentes precisa ser maior ou igual à quantidade de números a serem apostados e menor ou igual a 60.")
                continue
        except:
            print("\n*** Erro *** Entrada inválida ***")
            continue
        else:
            break

    aposta = random.sample(lista_numeros[0:nt],np) #escolhe a aposta com base nos parâmetros np, nt
    aposta.sort() #ordena os números a serem apostados

    ### impressão da saída
    print("\nAposta escolhida -", np, "números:") #imprime a aposta escolhida
    for k in range(len(aposta)):
        print("%3s" %aposta[k], end = '')

    print("\n\nSorteados há mais tempo -", nt, "números:") #imprime os números que serviram de base para a aposta
    for k in range(nt):
        print("%3s" %lista_numeros[k], end = '')
    print()





