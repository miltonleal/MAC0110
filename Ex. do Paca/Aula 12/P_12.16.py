# Escreva uma função que recebe um valor em segundos e devolve 3 valores que representam a
# quantidade de horas, minutos e segundos equivalentes.

def transforma_segundos (segundos):

    hor = segundos // 3600
    min = segundos % 3600 // 60
    seg = segundos % 60
    return hor, min, seg

print (transforma_segundos(1800))

#forma alternativa

def transforma_segundos (segundos):

    return segundos // 3600, segundos % 3600 // 60, segundos % 60

print (transforma_segundos(1800))

# exemplos de chamadas
v_seg = 1800

# recebendo o resultado numa tupla
a, b, c = transforma_segundos(v_seg)
print("h:", a, " m:", b, " s:", c)

# imprimindo a tupla diretamente
print("(horas, minutos, segundos):", transforma_segundos(v_seg))

# recebendo o resultado num objeto do tipo tupla
t = transforma_segundos(v_seg)
print("(horas, minutos, segundos):", t)

# imprimindo os elementos da tupla com índices
print("h:", t[0], " m:", t[1], " s:", t[2])

# atribuindo o objeto do tipo tupla a varíáveis independentes
t1, t2, t3 = t
print("h:", t1, " m:", t2, " s:", t3)