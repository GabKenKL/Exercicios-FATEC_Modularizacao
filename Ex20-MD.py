#Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

#declarar variáveis
A: int = 0
B: int = 0
C: int = 0
X1: float = 0
X2: float = 0
disc: float = 0

def discriminante():
    global disc
    disc = B**2 - 4 * A *C
    if (disc > 0):
        caso_maior()
    elif (disc == 0):
        caso_igual()
    elif (disc < 0):
        print("Não há raízes reais.")
        
def caso_maior():
    X1 = (-B + disc**(1/2)) / 2 * A
    X2 = (-B - disc**(1/2)) / 2 * A
    print("O valor das raízes são " , X1 , "e" , X2)

def caso_igual():
    X1 = (-B + disc**(1/2)) / 2 * A
    X2 = X1
    print("O valor das raízes é ", X2)

def main():
    global A
    global B
    global C
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))
    discriminante()

if (__name__ == '__main__'):
    main()
