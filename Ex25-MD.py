#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo
#em horas e minutos, sabendo que o tempo 
#máximo é menor que 24 horas e pode começar num dia e terminar noutro.

hora_inicial: int = 0
hora_final: int = 0
min_inicial: int = 0
min_final: int = 0
horas_totais: int = 0
min_totais: int = 0

def total_horas():
    global horas_totais    
    if hora_final < hora_inicial:
        h_24h = 24 - hora_inicial
        horas_totais = hora_final + h_24h
    else:
        horas_totais = hora_final - hora_inicial
    total_min()

def total_min():
    global min_totais
    global min_final
    global horas_totais
    if min_final < min_inicial:
        min_final = min_final + 60
        min_total = min_final - min_inicial
        horas_totais = horas_totais - 1
    else:
        min_total = min_final - min_inicial
    print("A duração do jogo foi de " , horas_totais, "horas e " , min_total , "minutos.")

def main():
    global hora_inicial
    global hora_final
    global min_inicial
    global min_final

    hora_inicial = int(input("Digite a hora inicial do jogo: "))
    hora_final = int(input("Digite a hora em que o jogo terminou: "))
    min_inicial= int(input("Digite em que minuto o jogo começou: "))
    min_final = int(input("Digite em que minuto o jogo acabou: "))
    total_horas()

if (__name__ == '__main__'):
    main()
