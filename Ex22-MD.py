#declaração de variáveis
N1: int = 0
N2: int = 0

def comparar():
    if N1 > N2:
        print("Em ordem crescente temos: " , N2 , "," , N1)
    else:
        print("Em ordem crescente temos: " , N1 , "," , N2)

def main():
    global N1
    global N2
    N1 = int(input("Digite o primeiro número: "))
    N2 = int(input("Digite o segundo número: "))
    comparar()

if (__name__ == '__main__'):
    main()
