#Dado um valor em segundos, transformá-lo para dias, horas, minutos e segundos.

def main ():

    #leia o número de segundos
    seg = int(input("Digite o número total de segundos: "))

    #calcula o número de dias
    dias = seg // 86400

    #calcula os segundos restantes dos dias
    seg_restante = seg % 86400

    #calcula o número de horas
    horas = seg_restante // 3600

    #calcula os segundos restantes das horas
    seg_restantes_min = seg_restante % 3600

    #calcula o número de minutos
    minutos = seg_restantes_min // 60

    #calcula os segundos restantes dos minutos
    segundos = seg_restantes_min % 60

    print ("O total de", seg, "segundo(s) representa(m)", dias, "dia(s)", horas, "hora(s)", minutos, "minuto(s) e", segundos, "segundo(s).")

main ()
