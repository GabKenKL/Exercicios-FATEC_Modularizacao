#algoritmo
#Declaração de variável
N1: float = 0
N2: float = 0
N3: float = 0
N4: float = 0
media: float = 0

def calc_media():
    global media
    media = (N1 + N2 + N3 + N4) / 4
    print("A média do aluno foi de: " , media)
    decisão()

def decisão():
    if media >= 6:
        print("APROVADO")
    elif media <= 3:
        print("RETIDO")
    else:
        print("EXAME")
    
def main():
    global N1
    global N2
    global N3
    global N4
    N1 = float(input("Digite a primeira nota: "))
    N2 = float(input("Digite a segunda nota: "))
    N3 = float(input("Digite a terceira nota: "))
    N4 = float(input("Digite a quarta nota: "))
    calc_media()

if (__name__ == '__main__'):
    main()
