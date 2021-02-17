def Criptografia(st, dsl):
    t = ''
    for i in range (len(st)):
        k = (ord(st[i]) + dsl) % 256
        t = t + chr(k)
    return t

print (Criptografia("Milton", 70))