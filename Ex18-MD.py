#declaração de variáveis
N1: int = 0
N2: int = 0

def diferença():
    if N1 > N2:
        difer = (N1 - N2)
    else:
        difer = (N2 - N1)
    print("A diferença entre o maior e o menor número equivale a" , difer)

def main():
    global N1
    global N2
    N1 = int(input("Digite o primeiro número: "))
    N2 = int(input("Digite o segundo número: "))
    diferença()

if (__name__ == '__main__'):
    main()