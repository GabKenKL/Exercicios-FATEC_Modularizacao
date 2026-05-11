#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

#declaração
N1: int = 0
N2: int = 0

def comparacao():
    if N1 > N2:
        if N1 % N2 == 0:
            print("O número " , N1 , "é multiplo de " , N2)
        else:
            print("O número " , N1 , "não é multiplo de " , N2)
    else:
        if N2 % N1 == 0:
            print("O número " , N2 , "é multiplo de " , N1)
        else:
            print("O número " , N2 , "não é multiplo de " , N1)



def main():
    global N1
    global N2

    N1 = int(input("Digite o primeiro número: "))
    N2 = int(input("Digite o segundo número: "))

    comparacao()

if (__name__ == '__main__'):
    main()
