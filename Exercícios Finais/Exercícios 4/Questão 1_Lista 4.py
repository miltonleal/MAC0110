# Escreva uma função Testa_String(st) que verifica se a string st é composta apenas por
# letras maiúsculas, minúsculas e espaços, devolvendo True ou False

def testa_string(st):

    for i in st: #varre a string para acessar os elementos
        if 0 <= ord(i) < 32 or 32 < ord(i) < 65 or 90 < ord(i) < 97 or ord(i) > 122: #compara com tabela ASCII
            return False
    return True

print(testa_string("213123"))

