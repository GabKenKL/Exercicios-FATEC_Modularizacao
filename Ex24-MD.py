#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

#declarar variável
N1: int = 0

def verificacao():
    if N1 % 2 == 0 and N1 % 3 == 0:
        print("O número" , N1 , "é divisível por 2 e 3.")
    else:
        print("O número" , N1 , "Não é divisível por 2 e 3.")

def main():
    global N1
    N1 = int(input("Digite um número: "))
    verificacao()

if (__name__ == '__main__'):
    main()
