#Escreva uma função media_final(p1, p2, ep1, ep2, ep3) que recebe as notas das provas p1 e p2 e
# as notas dos exercícios-programa ep1, ep2 e ep3 de um aluno. Devolve a média final deste aluno. A
# média final é dada por (3p+ep)/4, onde p = (p1+2p2)/3 e ep = (ep1+2ep2+3ep3)/6.
# Acrescentando se p < 5 ou ep < 5 a média final é o mínimo entre p e ep.

def main ():

    p1 = float (input("Digite a nota da P1: "))
    p2 = float(input("Digite a nota da P2: "))
    ep1 = float(input("Digite a nota do EP 1: "))
    ep2 = float(input("Digite a nota da EP 2: "))
    ep3 = float(input("Digite a nota da EP 3: "))

    print("A média final do aluno é: %2.1f" % media_final(p1, p2, ep1, ep2, ep3))

def media_final (p1,p2, ep1, ep2, ep3):

    p = (p1+(2*p2))/3
    ep = (ep1 + (2*ep2) + (3*ep3))/6

    if p < 5 or ep < 5:
        mf = min(p, ep)

    else:
        mf = ((3*p) + ep)/4

    return mf

main ()
