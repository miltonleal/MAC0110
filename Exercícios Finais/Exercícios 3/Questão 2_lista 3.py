def F(x, y):
    if y <= 0: return 0
    return x / y + F(x-1, y-1)

#print (F(1,2))

def F_non_recursive(x,y):

    resultado = 0 #inicia a variável resultado com zero
    while y>0: #executa o loop até atingir a condição de parada
        resultado += x/y #realiza a operação quociente
        x, y = x-1, y-1 #reduz uma unidade do x e do y
    return resultado

print(F_non_recursive(4,2))