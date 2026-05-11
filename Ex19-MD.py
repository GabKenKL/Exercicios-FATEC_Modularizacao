#Receba 2 valores reais. Calcule e mostre o maior deles.

N1: int = 0
N2: int = 0

def maior():
    if N1 > N2:
        print("O valor" , N1 , "é o maior.")
    else:
        print("O valor" , N2 , "é o maior.")

def main():
    global N1
    global N2
    N1 = int(input("Digite o primeiro número: "))
    N2 = int(input("Digite o segundo número: "))
    maior()

if (__name__ == '__main__'):
    main()
