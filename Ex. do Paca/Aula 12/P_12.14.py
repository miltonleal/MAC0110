#Função que devolve a frase “primeiro maior ou igual ao segundo” ou “primeiro menor que o segundo”.

def maior_ou_menor_string (x,y):

    if x>=y: return "primeiro maior ou igual ao segundo"
    return "primeiro menor que o segundo"

print (maior_ou_menor_string(4,3))
print (maior_ou_menor_string(2,3))
print (maior_ou_menor_string(7,3))
print (maior_ou_menor_string(1,3))
print (maior_ou_menor_string(9,3))
print (maior_ou_menor_string(3.4,3))
print (maior_ou_menor_string(2,3))
