#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

#declaração de variável
"""docstring"""
N1: float = 0
N2: float = 0
N3: float = 0
N4: float = 0

def quarto_N():
    global N4
    N4 = float(input("Digite o quarto número: "))
    if N4 < N1:
            print("Os valores em ordem crescente são:" , N4 , "," , N1 , "," , N2 , "e" , N3)
    elif N1 < N4 < N2:
         print("Os valores em ordem crescente são:" , N1 , "," , N4 , "," , N2 , "e" , N3)
    elif N2 < N4 < N3:
         print("Os valores em ordem crescente são:" , N1 , "," , N2 , "," , N4 , "e" , N3)
    elif N3 < N4:
         print("Os valores em ordem crescente são:" , N1 , "," , N2 , "," , N3 , "e" , N4)


def main():
    global N1
    global N2
    global N3
    print("Digite três números. Devem estar em ordem crescente!")
    N1 = float(input("Digite o primeiro número: "))
    N2 = float(input("Digite o segundo número: "))
    N3 = float(input("Digite o terceiro número: "))
    quarto_N()

if (__name__ == '__main__'):
     main()
